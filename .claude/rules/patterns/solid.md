# Principios SOLID

## 1. Single Responsibility Principle (SRP)

**Definición**: Una clase debe tener una sola razón para cambiar.

### Ejemplo (Python - Antes)
```python
class UserService:
    def create_user(self, data):
        # Validar
        # Guardar en DB
        # Enviar email de bienvenida
        # Loggear acción
        pass
```

### Ejemplo (Python - Después)
```python
class UserValidator:
    def validate(self, data):
        pass

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send_welcome(self, email):
        pass

class Logger:
    def log(self, message):
        pass

class UserService:
    def __init__(self, validator, repo, email, logger):
        self.validator = validator
        self.repo = repo
        self.email = email
        self.logger = logger
    
    def create_user(self, data):
        self.validator.validate(data)
        user = User(**data)
        self.repo.save(user)
        self.email.send_welcome(user.email)
        self.logger.log(f"User created: {user.id}")
```

### Ejemplo (TypeScript - Después)
```typescript
class UserValidator {
  validate(data: any): void {}
}

class UserRepository {
  save(user: User): void {}
}

class EmailService {
  sendWelcome(email: string): void {}
}

class Logger {
  log(message: string): void {}
}

class UserService {
  constructor(
    private validator: UserValidator,
    private repo: UserRepository,
    private email: EmailService,
    private logger: Logger
  ) {}
  
  createUser(data: any): void {
    this.validator.validate(data);
    const user = new User(data);
    this.repo.save(user);
    this.email.sendWelcome(user.email);
    this.logger.log(`User created: ${user.id}`);
  }
}
```

### Ejemplo (Go - Después)
```go
type UserValidator interface {
    Validate(data any) error
}

type UserRepository interface {
    Save(user User) error
}

type EmailService interface {
    SendWelcome(email string) error
}

type Logger interface {
    Log(message string)
}

type UserService struct {
    validator UserValidator
    repo      UserRepository
    email     EmailService
    logger    Logger
}

func (s *UserService) CreateUser(data any) error {
    if err := s.validator.Validate(data); err != nil {
        return err
    }
    user := NewUser(data)
    if err := s.repo.Save(user); err != nil {
        return err
    }
    s.email.SendWelcome(user.Email)
    s.logger.Log(fmt.Sprintf("User created: %s", user.ID))
    return nil
}
```

## 2. Open/Closed Principle (OCP)

**Definición**: Abierto para extensión, cerrado para modificación.

### Ejemplo (Python)
```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        # Lógica específica de tarjeta de crédito
        pass

class PayPalPayment(PaymentMethod):
    def process(self, amount):
        # Lógica específica de PayPal
        pass

class PaymentProcessor:
    def __init__(self):
        self.methods = []
    
    def register_method(self, method: PaymentMethod):
        self.methods.append(method)
    
    def process_payment(self, amount, method_name):
        for method in self.methods:
            if method.__class__.__name__ == method_name:
                return method.process(amount)
```

### Ejemplo (TypeScript)
```typescript
abstract class PaymentMethod {
  abstract process(amount: number): void;
}

class CreditCardPayment extends PaymentMethod {
  process(amount: number): void {
    // Lógica específica de tarjeta de crédito
  }
}

class PayPalPayment extends PaymentMethod {
  process(amount: number): void {
    // Lógica específica de PayPal
  }
}

class PaymentProcessor {
  private methods: PaymentMethod[] = [];
  
  registerMethod(method: PaymentMethod): void {
    this.methods.push(method);
  }
  
  processPayment(amount: number, methodType: string): void {
    const method = this.methods.find(m => m.constructor.name === methodType);
    method?.process(amount);
  }
}
```

### Ejemplo (Go)
```go
type PaymentMethod interface {
    Process(amount float64) error
}

type CreditCardPayment struct{}

func (c *CreditCardPayment) Process(amount float64) error {
    // Lógica específica de tarjeta de crédito
    return nil
}

type PayPalPayment struct{}

func (p *PayPalPayment) Process(amount float64) error {
    // Lógica específica de PayPal
    return nil
}

type PaymentProcessor struct {
    methods map[string]PaymentMethod
}

func (p *PaymentProcessor) RegisterMethod(name string, method PaymentMethod) {
    if p.methods == nil {
        p.methods = make(map[string]PaymentMethod)
    }
    p.methods[name] = method
}

func (p *PaymentProcessor) ProcessPayment(amount float64, methodType string) error {
    if method, ok := p.methods[methodType]; ok {
        return method.Process(amount)
    }
    return fmt.Errorf("payment method not found")
}
```

## 3. Liskov Substitution Principle (LSP)

**Definición**: Las subclases deben ser sustituibles por sus superclases.

### Ejemplo (Python - Violación)
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # VIOLA LSP
    
    def set_height(self, height):
        self.width = height  # VIOLA LSP
        self.height = height
```

### Ejemplo (Python - Correcto)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
```

### Ejemplo (TypeScript - Correcto)
```typescript
abstract class Shape {
  abstract area(): number;
}

class Rectangle extends Shape {
  constructor(private width: number, private height: number) {}
  
  area(): number {
    return this.width * this.height;
  }
}

class Square extends Shape {
  constructor(private side: number) {}
  
  area(): number {
    return this.side * this.side;
  }
}
```

### Ejemplo (Go - Correcto)
```go
type Shape interface {
    Area() float64
}

type Rectangle struct {
    Width  float64
    Height float64
}

func (r *Rectangle) Area() float64 {
    return r.Width * r.Height
}

type Square struct {
    Side float64
}

func (s *Square) Area() float64 {
    return s.Side * s.Side
}
```

## 4. Interface Segregation Principle (ISP)

**Definición**: Los clientes no deben depender de interfaces que no usan.

### Ejemplo (Python - Violación)
```python
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass

class Robot(Worker):  # Robot no necesita comer
    def work(self):
        pass
    
    def eat(self):
        raise NotImplementedError()  # VIOLA ISP
```

### Ejemplo (Python - Correcto)
```python
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Workable):  # Solo implementa lo que necesita
    def work(self):
        pass
```

### Ejemplo (TypeScript - Correcto)
```typescript
interface Workable {
  work(): void;
}

interface Eatable {
  eat(): void;
}

class Human implements Workable, Eatable {
  work(): void {}
  eat(): void {}
}

class Robot implements Workable {
  work(): void {}
}
```

### Ejemplo (Go - Correcto)
```go
type Workable interface {
    Work()
}

type Eatable interface {
    Eat()
}

type Human struct{}

func (h *Human) Work() {}
func (h *Human) Eat() {}

type Robot struct{}

func (r *Robot) Work() {}
```

## 5. Dependency Inversion Principle (DIP)

**Definición**: Depender de abstracciones, no de concreciones.

### Ejemplo (Python - Violación)
```python
class UserService:
    def __init__(self):
        self.db = PostgreSQLDatabase()  # DEPENDE DE CONCRECIÓN
```

### Ejemplo (Python - Correcto)
```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, entity):
        pass

class PostgreSQLDatabase(Database):
    def save(self, entity):
        # Implementación PostgreSQL
        pass

class MongoDBDatabase(Database):
    def save(self, entity):
        # Implementación MongoDB
        pass

class UserService:
    def __init__(self, db: Database):  # DEPENDE DE ABSTRACCIÓN
        self.db = db
```

### Ejemplo (TypeScript - Correcto)
```typescript
interface Database {
  save(entity: any): void;
}

class PostgreSQLDatabase implements Database {
  save(entity: any): void {
    // Implementación PostgreSQL
  }
}

class MongoDBDatabase implements Database {
  save(entity: any): void {
    // Implementación MongoDB
  }
}

class UserService {
  constructor(private db: Database) {}
}
```

### Ejemplo (Go - Correcto)
```go
type Database interface {
    Save(entity any) error
}

type PostgreSQLDatabase struct{}

func (p *PostgreSQLDatabase) Save(entity any) error {
    // Implementación PostgreSQL
    return nil
}

type MongoDBDatabase struct{}

func (m *MongoDBDatabase) Save(entity any) error {
    // Implementación MongoDB
    return nil
}

type UserService struct {
    db Database
}

func NewUserService(db Database) *UserService {
    return &UserService{db: db}
}
```

## Resumen

| Principio | Clave | Beneficio |
|-----------|-------|-----------|
| SRP | Una razón para cambiar | Código más fácil de mantener |
| OCP | Extensible sin modificar | Código más flexible |
| LSP | Sustituibilidad | Código más robusto |
| ISP | Interfaces específicas | Código más cohesivo |
| DIP | Depender de abstracciones | Código más desacoplado |
