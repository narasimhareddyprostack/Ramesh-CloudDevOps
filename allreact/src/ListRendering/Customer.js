import React, { Component } from "react";
import { customerStore } from "./customerStore";
class Customer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      customerList: customerStore,
    };
  }
  render() {
    return (
      <React.Fragment>
        <pre>{JSON.stringify(this.state.customerList)}</pre>
        <div className="container">
          <dic className="row">
            <div className="col">
              <p>Employee Info</p>
            </div>
          </dic>
          <dic className="row">
            <div className="col">
              <table className="table table-hover text-center table-striped table-light">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>age</th>
                    <th>Email</th>
                    <th>Location</th>
                  </tr>
                </thead>
                <tbody>
                  {this.state.employee.map((employee) => {
                    return (
                      <tr>
                        <td>{employee.id}</td>
                        <td>{employee.name}</td>
                        <td>{employee.age}</td>
                        <td>{employee.loc}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </dic>
        </div>
      </React.Fragment>
    );
  }
}

export default EmployeeList;
