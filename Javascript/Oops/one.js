/* 
What is Encapsulation

Encaspulation is defined as the wrapping up of data under a single unit

It is the mechanism that binds together code and the data.

The JS encapsulation is process of binding the data(ie variables) 
with the functions acting on the data

class = method + properties

Advantages of Encapsulation in JavaScript

    Encapsulation secure an object against illegal access.

    Encapsulation helps to achieve a level without revealing its complex details.
    This will reduce human errors.
    Make the application more flexible and manageable.
 */
class Order {
  constructor() {
    let orderId, orderStatus;
  }
  getOrderId() {
    return this.orderId;
  }
  setOrderId(id) {
    this.orderId = id;
  }
}
let x = new Order();
x.setOrderId(1);
console.log(x.getOrderId());
