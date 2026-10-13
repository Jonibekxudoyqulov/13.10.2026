// Asosiy (Ota) class
class Vehicle {
  constructor(brand, year) {
    this.brand = brand;
    this.year = year;
  }

  getInfo() {
    return `${this.brand} (${this.year}-yil)`;
  }
}

// Voris class (Vehicle klassidan namuna oladi)
class Car extends Vehicle {
  constructor(brand, year, model) {
    super(brand, year); // Ota klassning constructor'ini chaqirish
    this.model = model;
  }

  getDetails() {
    return `${this.getInfo()} - Model: ${this.model}`;
  }
}

// Ob'ekt yaratish
const myCar = new Car('Chevrolet', 2023, 'Gentra');
console.log(myCar.getDetails()); // Chevrolet (2023-yil) - Model: Gentra