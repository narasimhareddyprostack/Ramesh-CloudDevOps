import React, { Fragment } from "react";

class LandingPage extends React.Component {
  render() {
    return (
      <Fragment>
        <div className="landing">
          <div className="wrapper">
            <div className="text-white d-flex flex-column text-center justify-content-center align-items-center h-100">
              <h2 className="display-3">Welcome to Ultimate Vacations</h2>
              <p className="lead">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque
                culpa eius molestiae possimus totam. A, aspernatur enim
                explicabo inventore laudantium molestiae nesciunt optio qui rem
                repudiandae. Aliquid nemo quasi vitae?
              </p>
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}
export default LandingPage;
