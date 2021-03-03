import React, { Component } from "react";

class EmployeeList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      employee: [
        {
          id: 101,
          name: "Narasimha",
          age: 37,
          loc: "Bangalore",
        },
        {
          id: 102,
          name: "Dheeran",
          age: 37,
          loc: "Bangalore",
        },
      ],
    };
  }
  render() {
    return (
      <React.Fragment>
        <pre>{JSON.stringify(this.state.employee)}</pre>
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
