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
        <div className="form-check">
        <input type="checkbox" className="form-check-input" id="user-login-chkbox" name="export-checkbox-1" value="user-login"/>
        <label htmlFor="user-login-chkbox" className="form-check-label">User creation and last login</label><br/>
        <input type="checkbox" className="form-check-input"  id="user-reviews-chkbox" name="export-checkbox-2" value="reviews"/>
        <label htmlFor="user-reviews-chkbox" className="form-check-label"> Reviews created</label><br/>
        </div>
      </form>
      {/* {loginError && loginError.length > 0 && <Error errors={loginError} />} */}
    </div>
  );
};
export default ExportIndex;
