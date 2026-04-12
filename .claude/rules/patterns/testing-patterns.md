# Patrones de Testing

## 1. Test Pyramid

**Propósito**: Guía la distribución ideal de tests según su nivel y coste.

### Diagrama

```
        /\
       /E2E\       ← Tests de extremo a extremo (5-10%)
      /------\
     /Integration\ ← Tests de integración (20-30%)
    /------------\
   /    Unit      \← Tests unitarios (60-70%)
  /----------------\
```

### Reglas

| Nivel | Porcentaje | Velocidad | Coste | Qué prueba |
|-------|-----------|-----------|-------|-----------|
| Unitarios | 60-70% | Muy rápidos (ms) | Bajo | Lógica aislada |
| Integración | 20-30% | Rápidos (segundos) | Medio | Interacción entre componentes |
| E2E | 5-10% | Lentos (minutos) | Alto | Flujo completo del usuario |

### Ejemplo (Python - Pytest)
```python
# Tests Unitarios
def test_calculate_total():
    calculator = Calculator()
    assert calculator.calculate_total([10, 20, 30]) == 60

# Tests de Integración
def test_create_order_in_db():
    repo = OrderRepository(db_session)
    order = repo.create(Order(total=100))
    assert order.id is not None

# Tests E2E
def test_checkout_flow(selenium):
    selenium.get("https://shop.com/checkout")
    selenium.find_element(By.ID, "email").send_keys("test@test.com")
    selenium.find_element(By.ID, "submit").click()
    assert "Order confirmed" in selenium.page_source
```

## 2. AAA Pattern (Arrange-Act-Assert)

**Propósito**: Estructura clara de tres fases para cada test.

### Estructura

```
Arrange: Preparar el escenario del test
Act: Ejecutar la acción a probar
Assert: Verificar el resultado esperado
```

### Ejemplo (Python)
```python
def test_user_creation():
    # Arrange
    user_data = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    service = UserService()
    
    # Act
    user = service.create_user(user_data)
    
    # Assert
    assert user.id is not None
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
```

### Ejemplo (TypeScript - Jest)
```typescript
test("user creation", () => {
  // Arrange
  const userData = {
    name: "John Doe",
    email: "john@example.com"
  };
  const service = new UserService();

  // Act
  const user = service.createUser(userData);

  // Assert
  expect(user.id).toBeDefined();
  expect(user.name).toBe("John Doe");
  expect(user.email).toBe("john@example.com");
});
```

### Ejemplo (Go)
```go
func TestUserCreation(t *testing.T) {
    // Arrange
    userData := map[string]interface{}{
        "name":  "John Doe",
        "email": "john@example.com",
    }
    service := NewUserService()

    // Act
    user, err := service.CreateUser(userData)

    // Assert
    if err != nil {
        t.Fatalf("unexpected error: %v", err)
    }
    if user.ID == "" {
        t.Error("expected user ID to be set")
    }
    if user.Name != "John Doe" {
        t.Errorf("expected name 'John Doe', got '%s'", user.Name)
    }
}
```

## 3. Given-When-Then (Gherkin)

**Propósito**: Especificar comportamiento en lenguaje natural, ideal para BDD.

### Formato

```
Given: Contexto inicial del escenario
When: Acción que se realiza
Then: Resultado esperado
```

### Ejemplo (Python - Behave)
```gherkin
Feature: User Registration
  Scenario: Successful registration
    Given a user with valid data
    When the user submits the registration form
    Then the user should be created
    And a welcome email should be sent
```

### Ejemplo (TypeScript - Cucumber)
```gherkin
Feature: Shopping Cart
  Scenario: Add item to cart
    Given the user is on the product page
    When the user clicks "Add to Cart"
    Then the item should appear in the cart
    And the cart total should be updated
```

### Ejemplo (Go - Godog)
```gherkin
Feature: Order Processing
  Scenario: Process order successfully
    Given an order with items
    When the order is processed
    Then the order status should be "completed"
    And inventory should be updated
```

## 4. Test Doubles

**Propósito**: Reemplazar dependencias reales con implementaciones controladas.

### Tipos de Test Doubles

#### Dummy
Objeto vacío usado solo para cumplir con parámetros.

```python
# Python
def test_order_processing():
    dummy_logger = DummyLogger()  # No hace nada
    service = OrderService(dummy_logger)
    service.process_order(order)
```

#### Stub
Proporciona respuestas predefinidas a llamadas.

```python
# Python
class StubUserRepository:
    def find_by_id(self, user_id):
        return User(id=1, name="Test User")

def test_get_user():
    stub_repo = StubUserRepository()
    service = UserService(stub_repo)
    user = service.get_user(1)
    assert user.name == "Test User"
```

```typescript
// TypeScript
class StubUserRepository implements UserRepository {
  findById(id: number): User {
    return { id: 1, name: "Test User" };
  }
}

test("get user", () => {
  const stubRepo = new StubUserRepository();
  const service = new UserService(stubRepo);
  const user = service.getUser(1);
  expect(user.name).toBe("Test User");
});
```

#### Mock
Verifica que se llamaron métodos específicos con argumentos específicos.

```python
# Python - pytest-mock
def test_send_notification(mocker):
    mock_email_service = mocker.Mock()
    service = NotificationService(mock_email_service)
    
    service.send_notification("test@example.com", "Hello")
    
    mock_email_service.send.assert_called_once_with(
        "test@example.com", "Hello"
    )
```

```typescript
// TypeScript - Jest
test("send notification", () => {
  const mockEmailService = {
    send: jest.fn()
  };
  const service = new NotificationService(mockEmailService);
  
  service.sendNotification("test@example.com", "Hello");
  
  expect(mockEmailService.send).toHaveBeenCalledTimes(1);
  expect(mockEmailService.send).toHaveBeenCalledWith(
    "test@example.com", "Hello"
  );
});
```

```go
// Go - testify/mock
func TestSendNotification(t *testing.T) {
    mockEmailService := new(mocks.EmailService)
    mockEmailService.On("Send", "test@example.com", "Hello").Return(nil)
    
    service := NewNotificationService(mockEmailService)
    service.SendNotification("test@example.com", "Hello")
    
    mockEmailService.AssertExpectations(t)
}
```

#### Spy
Registra información sobre llamadas para verificación posterior.

```python
# Python
class SpyEmailService:
    def __init__(self):
        self.sent_emails = []
    
    def send(self, to, subject):
        self.sent_emails.append({"to": to, "subject": subject})

def test_email_spy():
    spy = SpyEmailService()
    service = NotificationService(spy)
    
    service.send_notification("test@example.com", "Hello")
    
    assert len(spy.sent_emails) == 1
    assert spy.sent_emails[0]["to"] == "test@example.com"
```

#### Fake
Implementación funcional pero simplificada.

```python
# Python - Fake en memoria
class InMemoryUserRepository:
    def __init__(self):
        self.users = {}
    
    def save(self, user):
        self.users[user.id] = user
    
    def find_by_id(self, user_id):
        return self.users.get(user_id)

def test_user_crud():
    fake_repo = InMemoryUserRepository()
    user = User(id=1, name="Test")
    
    fake_repo.save(user)
    retrieved = fake_repo.find_by_id(1)
    
    assert retrieved.name == "Test"
```

## 5. Page Object Model (POM)

**Propósito**: Abstraer la interacción con la UI en objetos reutilizables.

### Estructura

```
Page/
├── BasePage.ts
├── LoginPage.ts
├── DashboardPage.ts
└── tests/
    └── login.spec.ts
```

### Ejemplo (TypeScript - Playwright)

```typescript
// BasePage.ts
export class BasePage {
  constructor(protected page: Page) {}
  
  async goto(url: string) {
    await this.page.goto(url);
  }
  
  async click(selector: string) {
    await this.page.click(selector);
  }
  
  async fill(selector: string, value: string) {
    await this.page.fill(selector, value);
  }
}

// LoginPage.ts
export class LoginPage extends BasePage {
  readonly emailInput = '#email';
  readonly passwordInput = '#password';
  readonly submitButton = '#submit';
  
  async login(email: string, password: string) {
    await this.fill(this.emailInput, email);
    await this.fill(this.passwordInput, password);
    await this.click(this.submitButton);
  }
}

// login.spec.ts
test('successful login', async ({ page }) => {
  const loginPage = new LoginPage(page);
  
  await loginPage.goto('/login');
  await loginPage.login('test@example.com', 'password123');
  
  await expect(page).toHaveURL('/dashboard');
});
```

### Ejemplo (Python - Selenium)

```python
# LoginPage.py
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit")
    
    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

# test_login.py
def test_successful_login(selenium):
    login_page = LoginPage(selenium)
    login_page.login("test@example.com", "password123")
    assert "/dashboard" in selenium.current_url
```

## 6. Data-Driven Testing

**Propósito**: Ejecutar el mismo test con múltiples conjuntos de datos.

### Ejemplo (Python - Pytest)

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (0, 0),
    (-1, 1),
])
def test_square(input, expected):
    assert square(input) == expected

# O usando CSV
@pytest.mark.csv("test_data.csv")
def test_calculate_price(row):
    quantity = int(row["quantity"])
    price = float(row["price"])
    result = calculate_total(quantity, price)
    assert result == float(row["expected_total"])
```

### Ejemplo (TypeScript - Jest)

```typescript
describe("square", () => {
  const testCases = [
    { input: 2, expected: 4 },
    { input: 3, expected: 9 },
    { input: 0, expected: 0 },
    { input: -1, expected: 1 },
  ];
  
  testCases.forEach(({ input, expected }) => {
    test(`should return ${expected} when input is ${input}`, () => {
      expect(square(input)).toBe(expected);
    });
  });
});
```

### Ejemplo (Go)

```go
func TestSquare(t *testing.T) {
    testCases := []struct {
        input    int
        expected int
    }{
        {2, 4},
        {3, 9},
        {0, 0},
        {-1, 1},
    }
    
    for _, tc := range testCases {
        t.Run(fmt.Sprintf("input=%d", tc.input), func(t *testing.T) {
            result := square(tc.input)
            if result != tc.expected {
                t.Errorf("expected %d, got %d", tc.expected, result)
            }
        })
    }
}
```

## 7. Test Fixtures

**Propósito**: Configurar y limpiar el entorno de tests de forma consistente.

### Ejemplo (Python - Pytest)

```python
import pytest

@pytest.fixture
def db_session():
    # Setup
    session = create_test_session()
    session.begin_nested()
    
    yield session
    
    # Teardown
    session.rollback()
    session.close()

@pytest.fixture
def sample_user(db_session):
    user = User(name="Test User", email="test@example.com")
    db_session.add(user)
    db_session.commit()
    return user

def test_get_user(db_session, sample_user):
    repo = UserRepository(db_session)
    user = repo.find_by_id(sample_user.id)
    assert user.name == "Test User"
```

### Ejemplo (TypeScript - Jest)

```typescript
let db: Database;
let userService: UserService;

beforeAll(async () => {
  db = await createTestDatabase();
  userService = new UserService(db);
});

beforeEach(async () => {
  await db.clear();
});

afterAll(async () => {
  await db.close();
});

test("create user", async () => {
  const user = await userService.create({
    name: "Test User",
    email: "test@example.com"
  });
  expect(user.id).toBeDefined();
});
```

### Ejemplo (Go)

```go
func TestUserService(t *testing.T) {
    db := setupTestDB(t)
    defer db.Close()
    
    service := NewUserService(db)
    
    t.Run("create user", func(t *testing.T) {
        user, err := service.CreateUser(User{
            Name:  "Test User",
            Email: "test@example.com",
        })
        
        if err != nil {
            t.Fatalf("unexpected error: %v", err)
        }
        if user.ID == 0 {
            t.Error("expected user ID to be set")
        }
    })
}
```

## 8. Test Builders

**Propósito**: Crear objetos de test complejos de forma legible y mantenible.

### Ejemplo (Python)

```python
class UserBuilder:
    def __init__(self):
        self.user = User()
    
    def with_id(self, user_id):
        self.user.id = user_id
        return self
    
    def with_name(self, name):
        self.user.name = name
        return self
    
    def with_email(self, email):
        self.user.email = email
        return self
    
    def build(self):
        return self.user

# Uso
user = (UserBuilder()
        .with_id(1)
        .with_name("John Doe")
        .with_email("john@example.com")
        .build())
```

### Ejemplo (TypeScript)

```typescript
class UserBuilder {
  private user: Partial<User> = {};
  
  withId(id: number): this {
    this.user.id = id;
    return this;
  }
  
  withName(name: string): this {
    this.user.name = name;
    return this;
  }
  
  withEmail(email: string): this {
    this.user.email = email;
    return this;
  }
  
  build(): User {
    return this.user as User;
  }
}

// Uso
const user = new UserBuilder()
  .withId(1)
  .withName("John Doe")
  .withEmail("john@example.com")
  .build();
```

### Ejemplo (Go)

```go
type UserBuilder struct {
    user User
}

func NewUserBuilder() *UserBuilder {
    return &UserBuilder{user: User{}}
}

func (b *UserBuilder) WithID(id int) *UserBuilder {
    b.user.ID = id
    return b
}

func (b *UserBuilder) WithName(name string) *UserBuilder {
    b.user.Name = name
    return b
}

func (b *UserBuilder) WithEmail(email string) *UserBuilder {
    b.user.Email = email
    return b
}

func (b *UserBuilder) Build() User {
    return b.user
}

// Uso
user := NewUserBuilder().
    WithID(1).
    WithName("John Doe").
    WithEmail("john@example.com").
    Build()
```

## 9. Snapshot Testing

**Propósito**: Verificar que la salida de un componente no cambia inesperadamente.

### Ejemplo (TypeScript - Jest + React Testing Library)

```typescript
import { render } from '@testing-library/react';
import UserProfile from './UserProfile';

test('UserProfile snapshot', () => {
  const user = {
    id: 1,
    name: 'John Doe',
    email: 'john@example.com'
  };
  
  const { asFragment } = render(<UserProfile user={user} />);
  expect(asFragment()).toMatchSnapshot();
});
```

### Ejemplo (Python - syrupy)

```python
from syrupy.assertion import SnapshotAssertion

def test_user_to_dict(snapshot: SnapshotAssertion):
    user = User(id=1, name="John Doe", email="john@example.com")
    assert user.to_dict() == snapshot
```

## 10. Property-Based Testing

**Propósito**: Verificar que las propiedades de un sistema se cumplen para un rango de entradas aleatorias.

### Ejemplo (Python - Hypothesis)

```python
from hypothesis import given, strategies as st
import pytest

@given(st.integers(), st.integers())
def test_addition_commutativity(a, b):
    assert a + b == b + a

@given(st.lists(st.integers()))
def test_sorting_idempotent(lst):
    result1 = sorted(lst)
    result2 = sorted(result1)
    assert result1 == result2

@given(st.text())
def test_email_validation(email):
    if is_valid_email(email):
        assert "@" in email
        assert "." in email.split("@")[1]
```

### Ejemplo (Go - testing/quick)

```go
func TestReverseString(t *testing.T) {
    property := func(s string) bool {
        reversed := reverseString(s)
        return reverseString(reversed) == s
    }
    
    if err := quick.Check(property, nil); err != nil {
        t.Error(err)
    }
}

func TestAdditionCommutativity(t *testing.T) {
    property := func(a, b int) bool {
        return add(a, b) == add(b, a)
    }
    
    if err := quick.Check(property, nil); err != nil {
        t.Error(err)
    }
}
```

## 11. Test Names Convention

**Propósito**: Nombres de tests claros y descriptivos.

### Buenas Prácticas

```
✅ test_should_return_user_when_id_exists
✅ test_should_throw_error_when_user_not_found
✅ test_order_total_calculation_with_discount
❌ test_user
❌ test1
❌ test_it_works
```

### Ejemplo (Python)

```python
class TestUserService:
    def test_should_create_user_with_valid_data(self):
        pass
    
    def test_should_raise_error_when_email_is_invalid(self):
        pass
    
    def test_should_return_user_when_id_exists(self):
        pass
    
    def test_should_return_none_when_user_not_found(self):
        pass
```

### Ejemplo (TypeScript)

```typescript
describe('UserService', () => {
  test('should create user with valid data', () => {});
  
  test('should raise error when email is invalid', () => {});
  
  test('should return user when id exists', () => {});
  
  test('should return null when user not found', () => {});
});
```

### Ejemplo (Go)

```go
func TestUserService_CreateUser_ValidData(t *testing.T) {}

func TestUserService_CreateUser_InvalidEmail(t *testing.T) {}

func TestUserService_GetByID_UserExists(t *testing.T) {}

func TestUserService_GetByID_UserNotFound(t *testing.T) {}
```

## 12. Test Isolation

**Propósito**: Cada test debe ser independiente y no afectar a otros tests.

### Ejemplo (Python)

```python
import pytest

@pytest.fixture(autouse=True)
def reset_database():
    yield
    db.reset()  # Limpia DB después de cada test

def test_create_user():
    user = User(name="User 1")
    db.save(user)
    assert db.count(User) == 1

def test_another_create_user():
    user = User(name="User 2")
    db.save(user)
    assert db.count(User) == 1  # No afectado por el test anterior
```

### Ejemplo (TypeScript)

```typescript
describe('UserService', () => {
  beforeEach(() => {
    db.clear(); // Limpia DB antes de cada test
  });
  
  test('create user', async () => {
    await userService.create({ name: 'User 1' });
    expect(await db.count('User')).toBe(1);
  });
  
  test('another create user', async () => {
    await userService.create({ name: 'User 2' });
    expect(await db.count('User')).toBe(1);
  });
});
```

## Resumen de Patrones

| Patrón | Cuándo Usar | Beneficio |
|--------|------------|-----------|
| Test Pyramid | Planificar estrategia de tests | Balance óptimo velocidad/cobertura |
| AAA | Escribir tests unitarios | Estructura clara y mantenible |
| Given-When-Then | BDD y especificaciones | Lenguaje natural compartido |
| Test Doubles | Aislar dependencias | Tests rápidos y confiables |
| POM | Tests E2E/UI | Código reutilizable y mantenible |
| Data-Driven | Múltiples escenarios similares | Menos código duplicado |
| Fixtures | Setup/teardown repetitivo | Código DRY y consistente |
| Builders | Crear objetos complejos | Tests legibles |
| Snapshot | Verificar UI/serialización | Detección de cambios no intencionados |
| Property-Based | Verificar propiedades generales | Bugs en edge cases |
| Good Naming | Siempre | Tests auto-documentados |
| Isolation | Siempre | Tests confiables y determinísticos |
