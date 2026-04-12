# Patrones de Diseño

## Patrones Creacionales

### 1. Factory Method

**Propósito**: Definir una interfaz para crear objetos, pero dejar que las subclases decidan qué clase instanciar.

### Ejemplo (Python)
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

# Uso
dog_factory = DogFactory()
dog = dog_factory.create_animal()
dog.make_sound()  # "Woof!"
```

### Ejemplo (TypeScript)
```typescript
interface Animal {
  makeSound(): string;
}

class Dog implements Animal {
  makeSound(): string {
    return "Woof!";
  }
}

class Cat implements Animal {
  makeSound(): string {
    return "Meow!";
  }
}

abstract class AnimalFactory {
  abstract createAnimal(): Animal;
}

class DogFactory extends AnimalFactory {
  createAnimal(): Animal {
    return new Dog();
  }
}

class CatFactory extends AnimalFactory {
  createAnimal(): Animal {
    return new Cat();
  }
}

// Uso
const dogFactory = new DogFactory();
const dog = dogFactory.createAnimal();
console.log(dog.makeSound()); // "Woof!"
```

### Ejemplo (Go)
```go
type Animal interface {
    MakeSound() string
}

type Dog struct{}

func (d *Dog) MakeSound() string {
    return "Woof!"
}

type Cat struct{}

func (c *Cat) MakeSound() string {
    return "Meow!"
}

type AnimalFactory interface {
    CreateAnimal() Animal
}

type DogFactory struct{}

func (f *DogFactory) CreateAnimal() Animal {
    return &Dog{}
}

type CatFactory struct{}

func (f *CatFactory) CreateAnimal() Animal {
    return &Cat{}
}
```

### 2. Builder

**Propósito**: Separar la construcción de un objeto complejo de su representación.

### Ejemplo (Python)
```python
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.bacon = False

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def add_bacon(self):
        self.pizza.bacon = True
        return self
    
    def build(self):
        return self.pizza

# Uso
pizza = (PizzaBuilder()
         .set_size("Large")
         .add_cheese()
         .add_pepperoni()
         .build())
```

### Ejemplo (TypeScript)
```typescript
class Pizza {
  size?: string;
  cheese = false;
  pepperoni = false;
  bacon = false;
}

class PizzaBuilder {
  private pizza: Pizza = new Pizza();
  
  setSize(size: string): this {
    this.pizza.size = size;
    return this;
  }
  
  addCheese(): this {
    this.pizza.cheese = true;
    return this;
  }
  
  addPepperoni(): this {
    this.pizza.pepperoni = true;
    return this;
  }
  
  addBacon(): this {
    this.pizza.bacon = true;
    return this;
  }
  
  build(): Pizza {
    return this.pizza;
  }
}

// Uso
const pizza = new PizzaBuilder()
  .setSize("Large")
  .addCheese()
  .addPepperoni()
  .build();
```

### Ejemplo (Go)
```go
type Pizza struct {
    Size      string
    Cheese    bool
    Pepperoni bool
    Bacon     bool
}

type PizzaBuilder struct {
    pizza *Pizza
}

func NewPizzaBuilder() *PizzaBuilder {
    return &PizzaBuilder{pizza: &Pizza{}}
}

func (b *PizzaBuilder) SetSize(size string) *PizzaBuilder {
    b.pizza.Size = size
    return b
}

func (b *PizzaBuilder) AddCheese() *PizzaBuilder {
    b.pizza.Cheese = true
    return b
}

func (b *PizzaBuilder) AddPepperoni() *PizzaBuilder {
    b.pizza.Pepperoni = true
    return b
}

func (b *PizzaBuilder) AddBacon() *PizzaBuilder {
    b.pizza.Bacon = true
    return b
}

func (b *PizzaBuilder) Build() *Pizza {
    return b.pizza
}

// Uso
pizza := NewPizzaBuilder().
    SetSize("Large").
    AddCheese().
    AddPepperoni().
    Build()
```

### 3. Singleton

**Propósito**: Asegurar que una clase tenga una única instancia y proporcionar un punto de acceso global.

**⚠️ ADVERTENCIA**: El Singleton es a menudo considerado un anti-patrón porque introduce estado global y hace difícil el testing. Úsalo con precaución.

### Ejemplo (Python - Thread-Safe)
```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# Uso
s1 = Singleton()
s2 = Singleton()
s1 is s2  # True
```

### Ejemplo (TypeScript)
```typescript
class Singleton {
  private static instance: Singleton;
  
  private constructor() {}
  
  static getInstance(): Singleton {
    if (!Singleton.instance) {
      Singleton.instance = new Singleton();
    }
    return Singleton.instance;
  }
}

// Uso
const s1 = Singleton.getInstance();
const s2 = Singleton.getInstance();
console.log(s1 === s2); // true
```

### Ejemplo (Go - Sync.Once)
```go
import "sync"

type Singleton struct{}

var (
    instance *Singleton
    once     sync.Once
)

func GetSingleton() *Singleton {
    once.Do(func() {
        instance = &Singleton{}
    })
    return instance
}
```

## Patrones Estructurales

### 4. Adapter

**Propósito**: Convertir la interfaz de una clase en otra interfaz que los clientes esperan.

### Ejemplo (Python)
```python
class MediaPlayer:
    def play(self, audio_type, filename):
        pass

class AdvancedMediaPlayer:
    def play_vlc(self, filename):
        pass
    
    def play_mp4(self, filename):
        pass

class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        self.advanced_player = AdvancedMediaPlayer()
    
    def play(self, audio_type, filename):
        if audio_type == "vlc":
            self.advanced_player.play_vlc(filename)
        elif audio_type == "mp4":
            self.advanced_player.play_mp4(filename)

class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.media_adapter = None
    
    def play(self, audio_type, filename):
        if audio_type in ["mp3", "wav"]:
            print(f"Playing {audio_type}: {filename}")
        else:
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, filename)

# Uso
player = AudioPlayer()
player.play("mp3", "song.mp3")
player.play("vlc", "movie.vlc")
```

### Ejemplo (TypeScript)
```typescript
interface MediaPlayer {
  play(audioType: string, filename: string): void;
}

class AdvancedMediaPlayer {
  playVlc(filename: string): void {
    console.log(`Playing VLC: ${filename}`);
  }
  
  playMp4(filename: string): void {
    console.log(`Playing MP4: ${filename}`);
  }
}

class MediaAdapter implements MediaPlayer {
  private advancedPlayer = new AdvancedMediaPlayer();
  
  play(audioType: string, filename: string): void {
    if (audioType === "vlc") {
      this.advancedPlayer.playVlc(filename);
    } else if (audioType === "mp4") {
      this.advancedPlayer.playMp4(filename);
    }
  }
}

class AudioPlayer implements MediaPlayer {
  private mediaAdapter?: MediaAdapter;
  
  play(audioType: string, filename: string): void {
    if (["mp3", "wav"].includes(audioType)) {
      console.log(`Playing ${audioType}: ${filename}`);
    } else {
      this.mediaAdapter = new MediaAdapter();
      this.mediaAdapter.play(audioType, filename);
    }
  }
}
```

### Ejemplo (Go)
```go
type MediaPlayer interface {
    Play(audioType, filename string)
}

type AdvancedMediaPlayer struct{}

func (a *AdvancedMediaPlayer) PlayVlc(filename string) {
    fmt.Printf("Playing VLC: %s\n", filename)
}

func (a *AdvancedMediaPlayer) PlayMp4(filename string) {
    fmt.Printf("Playing MP4: %s\n", filename)
}

type MediaAdapter struct {
    advancedPlayer *AdvancedMediaPlayer
}

func (m *MediaAdapter) Play(audioType, filename string) {
    if audioType == "vlc" {
        m.advancedPlayer.PlayVlc(filename)
    } else if audioType == "mp4" {
        m.advancedPlayer.PlayMp4(filename)
    }
}

type AudioPlayer struct {
    mediaAdapter *MediaAdapter
}

func (a *AudioPlayer) Play(audioType, filename string) {
    if audioType == "mp3" || audioType == "wav" {
        fmt.Printf("Playing %s: %s\n", audioType, filename)
    } else {
        a.mediaAdapter = &MediaAdapter{advancedPlayer: &AdvancedMediaPlayer{}}
        a.mediaAdapter.Play(audioType, filename)
    }
}
```

### 5. Decorator

**Propósito**: Añadir responsabilidades adicionales a un objeto dinámicamente.

### Ejemplo (Python)
```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Sending email: {message}")

class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped
    
    def send(self, message):
        self._wrapped.send(message)

class SlackDecorator(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Sending Slack: {message}")

class SMSDecorator(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Sending SMS: {message}")

# Uso
notifier = EmailNotifier()
notifier = SlackDecorator(notifier)
notifier = SMSDecorator(notifier)
notifier.send("Hello World!")
```

### Ejemplo (TypeScript)
```typescript
abstract class Notifier {
  abstract send(message: string): void;
}

class EmailNotifier extends Notifier {
  send(message: string): void {
    console.log(`Sending email: ${message}`);
  }
}

abstract class NotifierDecorator extends Notifier {
  constructor(protected wrapped: Notifier) {
    super();
  }
  
  send(message: string): void {
    this.wrapped.send(message);
  }
}

class SlackDecorator extends NotifierDecorator {
  send(message: string): void {
    super.send(message);
    console.log(`Sending Slack: ${message}`);
  }
}

class SMSDecorator extends NotifierDecorator {
  send(message: string): void {
    super.send(message);
    console.log(`Sending SMS: ${message}`);
  }
}

// Uso
let notifier: Notifier = new EmailNotifier();
notifier = new SlackDecorator(notifier);
notifier = new SMSDecorator(notifier);
notifier.send("Hello World!");
```

### Ejemplo (Go)
```go
type Notifier interface {
    Send(message string)
}

type EmailNotifier struct{}

func (e *EmailNotifier) Send(message string) {
    fmt.Printf("Sending email: %s\n", message)
}

type SlackDecorator struct {
    wrapped Notifier
}

func (s *SlackDecorator) Send(message string) {
    s.wrapped.Send(message)
    fmt.Printf("Sending Slack: %s\n", message)
}

type SMSDecorator struct {
    wrapped Notifier
}

func (s *SMSDecorator) Send(message string) {
    s.wrapped.Send(message)
    fmt.Printf("Sending SMS: %s\n", message)
}
```

### 6. Facade

**Propósito**: Proporcionar una interfaz simplificada a una biblioteca, un framework u otro conjunto complejo de clases.

### Ejemplo (Python)
```python
class SubsystemA:
    def operation_a(self):
        return "SubsystemA: Operation A"

class SubsystemB:
    def operation_b(self):
        return "SubsystemB: Operation B"

class SubsystemC:
    def operation_c(self):
        return "SubsystemC: Operation C"

class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()
    
    def operation(self):
        results = []
        results.append(self.subsystem_a.operation_a())
        results.append(self.subsystem_b.operation_b())
        results.append(self.subsystem_c.operation_c())
        return results

# Uso
facade = Facade()
results = facade.operation()
```

### Ejemplo (TypeScript)
```typescript
class SubsystemA {
  operationA(): string {
    return "SubsystemA: Operation A";
  }
}

class SubsystemB {
  operationB(): string {
    return "SubsystemB: Operation B";
  }
}

class SubsystemC {
  operationC(): string {
    return "SubsystemC: Operation C";
  }
}

class Facade {
  private subsystemA = new SubsystemA();
  private subsystemB = new SubsystemB();
  private subsystemC = new SubsystemC();
  
  operation(): string[] {
    return [
      this.subsystemA.operationA(),
      this.subsystemB.operationB(),
      this.subsystemC.operationC()
    ];
  }
}

// Uso
const facade = new Facade();
const results = facade.operation();
```

### Ejemplo (Go)
```go
type SubsystemA struct{}

func (s *SubsystemA) OperationA() string {
    return "SubsystemA: Operation A"
}

type SubsystemB struct{}

func (s *SubsystemB) OperationB() string {
    return "SubsystemB: Operation B"
}

type SubsystemC struct{}

func (s *SubsystemC) OperationC() string {
    return "SubsystemC: Operation C"
}

type Facade struct {
    subsystemA *SubsystemA
    subsystemB *SubsystemB
    subsystemC *SubsystemC
}

func NewFacade() *Facade {
    return &Facade{
        subsystemA: &SubsystemA{},
        subsystemB: &SubsystemB{},
        subsystemC: &SubsystemC{},
    }
}

func (f *Facade) Operation() []string {
    return []string{
        f.subsystemA.OperationA(),
        f.subsystemB.OperationB(),
        f.subsystemC.OperationC(),
    }
}
```

## Patrones de Comportamiento

### 7. Strategy

**Propósito**: Definir una familia de algoritmos, encapsular cada uno y hacerlos intercambiables.

### Ejemplo (Python)
```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with Credit Card")

class PayPalStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with PayPal")

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item):
        self.items.append(item)
    
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy
    
    def checkout(self):
        total = sum(item['price'] for item in self.items)
        self.payment_strategy.pay(total)

# Uso
cart = ShoppingCart()
cart.add_item({'name': 'Item 1', 'price': 100})
cart.set_payment_strategy(CreditCardStrategy())
cart.checkout()
```

### Ejemplo (TypeScript)
```typescript
interface PaymentStrategy {
  pay(amount: number): void;
}

class CreditCardStrategy implements PaymentStrategy {
  pay(amount: number): void {
    console.log(`Paid $${amount} with Credit Card`);
  }
}

class PayPalStrategy implements PaymentStrategy {
  pay(amount: number): void {
    console.log(`Paid $${amount} with PayPal`);
  }
}

class ShoppingCart {
  private items: { name: string; price: number }[] = [];
  private paymentStrategy?: PaymentStrategy;
  
  addItem(item: { name: string; price: number }): void {
    this.items.push(item);
  }
  
  setPaymentStrategy(strategy: PaymentStrategy): void {
    this.paymentStrategy = strategy;
  }
  
  checkout(): void {
    const total = this.items.reduce((sum, item) => sum + item.price, 0);
    this.paymentStrategy?.pay(total);
  }
}

// Uso
const cart = new ShoppingCart();
cart.addItem({ name: 'Item 1', price: 100 });
cart.setPaymentStrategy(new CreditCardStrategy());
cart.checkout();
```

### Ejemplo (Go)
```go
type PaymentStrategy interface {
    Pay(amount float64)
}

type CreditCardStrategy struct{}

func (c *CreditCardStrategy) Pay(amount float64) {
    fmt.Printf("Paid $%.2f with Credit Card\n", amount)
}

type PayPalStrategy struct{}

func (p *PayPalStrategy) Pay(amount float64) {
    fmt.Printf("Paid $%.2f with PayPal\n", amount)
}

type ShoppingCart struct {
    items          []Item
    paymentStrategy PaymentStrategy
}

type Item struct {
    Name  string
    Price float64
}

func (c *ShoppingCart) AddItem(item Item) {
    c.items = append(c.items, item)
}

func (c *ShoppingCart) SetPaymentStrategy(strategy PaymentStrategy) {
    c.paymentStrategy = strategy
}

func (c *ShoppingCart) Checkout() {
    total := 0.0
    for _, item := range c.items {
        total += item.Price
    }
    c.paymentStrategy.Pay(total)
}
```

### 8. Observer

**Propósito**: Definir una dependencia uno-a-muchos entre objetos, de manera que cuando un objeto cambia su estado, todos sus dependientes son notificados.

### Ejemplo (Python)
```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class NewsPublisher(Subject):
    def publish_news(self, news):
        self.notify(news)

class EmailSubscriber(Observer):
    def update(self, message):
        print(f"Email received: {message}")

class SMSSubscriber(Observer):
    def update(self, message):
        print(f"SMS received: {message}")

# Uso
publisher = NewsPublisher()
publisher.attach(EmailSubscriber())
publisher.attach(SMSSubscriber())
publisher.publish_news("Breaking news!")
```

### Ejemplo (TypeScript)
```typescript
interface Observer {
  update(message: string): void;
}

abstract class Subject {
  private observers: Observer[] = [];
  
  attach(observer: Observer): void {
    this.observers.push(observer);
  }
  
  detach(observer: Observer): void {
    this.observers = this.observers.filter(o => o !== observer);
  }
  
  notify(message: string): void {
    this.observers.forEach(o => o.update(message));
  }
}

class NewsPublisher extends Subject {
  publishNews(news: string): void {
    this.notify(news);
  }
}

class EmailSubscriber implements Observer {
  update(message: string): void {
    console.log(`Email received: ${message}`);
  }
}

class SMSSubscriber implements Observer {
  update(message: string): void {
    console.log(`SMS received: ${message}`);
  }
}

// Uso
const publisher = new NewsPublisher();
publisher.attach(new EmailSubscriber());
publisher.attach(new SMSSubscriber());
publisher.publishNews("Breaking news!");
```

### Ejemplo (Go)
```go
type Observer interface {
    Update(message string)
}

type Subject struct {
    observers []Observer
}

func (s *Subject) Attach(observer Observer) {
    s.observers = append(s.observers, observer)
}

func (s *Subject) Detach(observer Observer) {
    for i, obs := range s.observers {
        if obs == observer {
            s.observers = append(s.observers[:i], s.observers[i+1:]...)
            break
        }
    }
}

func (s *Subject) Notify(message string) {
    for _, observer := range s.observers {
        observer.Update(message)
    }
}

type NewsPublisher struct {
    Subject
}

func (n *NewsPublisher) PublishNews(news string) {
    n.Notify(news)
}

type EmailSubscriber struct{}

func (e *EmailSubscriber) Update(message string) {
    fmt.Printf("Email received: %s\n", message)
}

type SMSSubscriber struct{}

func (s *SMSSubscriber) Update(message string) {
    fmt.Printf("SMS received: %s\n", message)
}
```

### 9. Command

**Propósito**: Encapsular una solicitud como un objeto, permitiendo así parametrizar clientes con diferentes solicitudes, encolar solicitudes o registrar operaciones.

### Ejemplo (Python)
```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def turn_on(self):
        print("Light is ON")
    
    def turn_off(self):
        print("Light is OFF")

class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.commands = []
    
    def set_command(self, command):
        self.commands.append(command)
    
    def press_button(self):
        for command in self.commands:
            command.execute()
        self.commands = []

# Uso
remote = RemoteControl()
light = Light()
remote.set_command(TurnOnCommand(light))
remote.press_button()
```

### Ejemplo (TypeScript)
```typescript
interface Command {
  execute(): void;
}

class Light {
  turnOn(): void {
    console.log("Light is ON");
  }
  
  turnOff(): void {
    console.log("Light is OFF");
  }
}

class TurnOnCommand implements Command {
  constructor(private light: Light) {}
  
  execute(): void {
    this.light.turnOn();
  }
}

class TurnOffCommand implements Command {
  constructor(private light: Light) {}
  
  execute(): void {
    this.light.turnOff();
  }
}

class RemoteControl {
  private commands: Command[] = [];
  
  setCommand(command: Command): void {
    this.commands.push(command);
  }
  
  pressButton(): void {
    this.commands.forEach(cmd => cmd.execute());
    this.commands = [];
  }
}

// Uso
const remote = new RemoteControl();
const light = new Light();
remote.setCommand(new TurnOnCommand(light));
remote.pressButton();
```

### Ejemplo (Go)
```go
type Command interface {
    Execute()
}

type Light struct{}

func (l *Light) TurnOn() {
    fmt.Println("Light is ON")
}

func (l *Light) TurnOff() {
    fmt.Println("Light is OFF")
}

type TurnOnCommand struct {
    light *Light
}

func (t *TurnOnCommand) Execute() {
    t.light.TurnOn()
}

type TurnOffCommand struct {
    light *Light
}

func (t *TurnOffCommand) Execute() {
    t.light.TurnOff()
}

type RemoteControl struct {
    commands []Command
}

func (r *RemoteControl) SetCommand(command Command) {
    r.commands = append(r.commands, command)
}

func (r *RemoteControl) PressButton() {
    for _, command := range r.commands {
        command.Execute()
    }
    r.commands = nil
}
```

### 10. Chain of Responsibility

**Propósito**: Evitar acoplar el emisor de una solicitud a su receptor, dando a más de un objeto la oportunidad de manejar la solicitud.

### Ejemplo (Python)
```python
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None
    
    def set_next(self, handler):
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(Handler):
    def handle(self, request):
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        return super().handle(request)

class SquirrelHandler(Handler):
    def handle(self, request):
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        return super().handle(request)

class DogHandler(Handler):
    def handle(self, request):
        if request == "Meat":
            return f"Dog: I'll eat the {request}"
        return super().handle(request)

# Uso
monkey = MonkeyHandler()
squirrel = SquirrelHandler()
dog = DogHandler()

monkey.set_next(squirrel).set_next(dog)
print(monkey.handle("Nut"))
```

### Ejemplo (TypeScript)
```typescript
abstract class Handler {
  private nextHandler?: Handler;
  
  setNext(handler: Handler): Handler {
    this.nextHandler = handler;
    return handler;
  }
  
  handle(request: string): string | null {
    return this.nextHandler?.handle(request) ?? null;
  }
}

class MonkeyHandler extends Handler {
  handle(request: string): string | null {
    if (request === "Banana") {
      return `Monkey: I'll eat the ${request}`;
    }
    return super.handle(request);
  }
}

class SquirrelHandler extends Handler {
  handle(request: string): string | null {
    if (request === "Nut") {
      return `Squirrel: I'll eat the ${request}`;
    }
    return super.handle(request);
  }
}

class DogHandler extends Handler {
  handle(request: string): string | null {
    if (request === "Meat") {
      return `Dog: I'll eat the ${request}`;
    }
    return super.handle(request);
  }
}

// Uso
const monkey = new MonkeyHandler();
const squirrel = new SquirrelHandler();
const dog = new DogHandler();

monkey.setNext(squirrel).setNext(dog);
console.log(monkey.handle("Nut"));
```

### Ejemplo (Go)
```go
type Handler interface {
    SetNext(handler Handler) Handler
    Handle(request string) string
}

type BaseHandler struct {
    nextHandler Handler
}

func (h *BaseHandler) SetNext(handler Handler) Handler {
    h.nextHandler = handler
    return handler
}

func (h *BaseHandler) Handle(request string) string {
    if h.nextHandler != nil {
        return h.nextHandler.Handle(request)
    }
    return ""
}

type MonkeyHandler struct {
    BaseHandler
}

func (m *MonkeyHandler) Handle(request string) string {
    if request == "Banana" {
        return fmt.Sprintf("Monkey: I'll eat the %s", request)
    }
    return m.BaseHandler.Handle(request)
}

type SquirrelHandler struct {
    BaseHandler
}

func (s *SquirrelHandler) Handle(request string) string {
    if request == "Nut" {
        return fmt.Sprintf("Squirrel: I'll eat the %s", request)
    }
    return s.BaseHandler.Handle(request)
}

type DogHandler struct {
    BaseHandler
}

func (d *DogHandler) Handle(request string) string {
    if request == "Meat" {
        return fmt.Sprintf("Dog: I'll eat the %s", request)
    }
    return d.BaseHandler.Handle(request)
}
```
