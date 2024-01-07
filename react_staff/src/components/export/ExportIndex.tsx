import React, { useEffect, useState } from "react";
import Error from "../../common/Error";
import "react-toastify/dist/ReactToastify.css";
import createAxiosInstance from "../../axiosInstance";
import { useNavigate } from "react-router-dom";
import { Export, ExportStatus, statusDisplayNames } from "../../interfaces/Export";
import { ToastType, useNotification } from "../../contexts/NotificationContext";
import { LoggedInUser } from "../../interfaces/LoginInterfaces";
import { useAppSelector } from "../../store/store";
import { format } from 'date-fns';
import { faDownload } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import axios from "axios";
import fileDownload from "js-file-download";

const ExportIndex: React.FC = () => {
  const [currentPageExports, setCurrentPageExports] = useState<Export[]>([]);
  const axiosInstance = createAxiosInstance(useNavigate(), useNotification());
  const notificationHook = useNotification();
  const loggedInUser: LoggedInUser = useAppSelector(
    (state) => state.loginUser.loggedInUser,
  );
  //use useeffect to call a method right after rendering
  // and also for cleanup
  useEffect(() => {
    const exportfetchUrl:string = `http://localhost:8005/user-service/export-app/exports`;
    const fetchExports= async () => {
      await axiosInstance
        .get(exportfetchUrl, {
          headers: {
            Authorization: `Bearer ${loggedInUser.token}`,
            // Add any other headers if needed
          },
        })
        .then((response) => {
          setCurrentPageExports(response.data);
          console.log("data is", response.data);
        })
        .catch((error) => {
          console.error("Error fetching exports:", error);
        });
    };
    if(loggedInUser){
      fetchExports();
    }
  }, [loggedInUser]);

  const handleDownload = async (task_id:string) => {
    const apiUrl = `http://localhost:8005/user-service/export-app/exports/download/${task_id}`;
    try{
      await axios.get(apiUrl, {
        responseType: 'blob',
      }).then(res => {
        const contentDisposition = res.headers['content-disposition'];
        const filenameMatch = contentDisposition && contentDisposition.match(/filename="([^"]+)"/);
        const filename = filenameMatch ? filenameMatch[1] : 'export-file.xlsx';
        fileDownload(res.data, filename);
      });
    }catch(err){
      console.log("file download error:",err)
      notificationHook.showNotification("File download failed", {
        type: ToastType.Error,
      });
    }
    

};



  return (
    <div className="container mt-5">
      <h2 className="mb-4">My Exports</h2>
  <table className="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Export initiated by</th>
      <th scope="col">Time</th>
      <th scope="col">Status</th>
      <th scope="col">Download link</th>
    </tr>
  </thead>
  <tbody>
  {
  currentPageExports.map((exportItem) => (
    <tr key={exportItem.id}>
      <th scope="row">{exportItem.id}</th>
      <td>{exportItem.creator.username}</td>
      <td>{format(exportItem.created_at, "do MMM yyyy h:mma")}</td>
      <td>{statusDisplayNames[exportItem.status]}</td>
      <td>
        {exportItem.status==ExportStatus.COMPLETED?
        <FontAwesomeIcon icon={faDownload} onClick={() => handleDownload(exportItem.task_id)} />:"-"}
        </td>
    </tr>
  ))
}

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
