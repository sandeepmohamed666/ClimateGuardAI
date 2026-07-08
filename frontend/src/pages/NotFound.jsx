import React from "react";
import { Link } from "react-router-dom";

const NotFound = () => {
  return (
    <section className="card">
      <h1>Page Not Found</h1>
      <p>The route does not exist in this build.</p>
      <Link to="/">Go to Dashboard</Link>
    </section>
  );
};

export default NotFound;
