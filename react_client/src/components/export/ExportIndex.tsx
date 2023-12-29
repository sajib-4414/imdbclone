import React, { useState } from "react";
import Error from "../../common/Error";
import "react-toastify/dist/ReactToastify.css";


const ExportIndex: React.FC = () => {

  return (
    <div className="container mt-5">
      <h2 className="mb-4">My Exports</h2>
  <table className="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Export initiated time</th>
      <th scope="col">Completed</th>
      <th scope="col">Download link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    
    <tr>
      <th scope="row">3</th>
      <td>Larry</td>
      <td>the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
<h2 className="mb-4">Create a new export</h2>
      <form>
        <div>
            <input type="checkbox">My reviews</input>
        </div>
      </form>
      {/* {loginError && loginError.length > 0 && <Error errors={loginError} />} */}
    </div>
  );
};
export default ExportIndex;
