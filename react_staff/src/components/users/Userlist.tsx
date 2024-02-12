import React, { useEffect, useState } from "react";
import { ToastType, useNotification } from "../../contexts/NotificationContext";
import createAxiosInstance from "../../axiosInstance";
import { Link, useNavigate } from "react-router-dom";
import { LoggedInUser } from "../../interfaces/LoginInterfaces";
import { useAppSelector } from "../../store/store";


const UserList: React.FC = () => {
    const [userList, setUserList] = useState([])
    const [selectedDeleteCheckboxes, setSelectedDeleteCheckboxes] = useState([]);
    const notificationHook = useNotification();
    const axiosInstance = createAxiosInstance(useNavigate(), useNotification());
    const loggedInUser: LoggedInUser = useAppSelector(
        (state) => state.loginUser.loggedInUser,
    );
    interface CheckboxState {
        'export-checkbox-creation-last-login': boolean;
        'export-checkbox-review-created': boolean;
    }
    const handleCheckboxChange = (name: keyof CheckboxState) => {
        setCheckboxes((prevState) => ({
          ...prevState,
          [name]: !prevState[name],
        }));
    };
    const [checkboxes, setCheckboxes] = useState<CheckboxState>({
        'export-checkbox-creation-last-login': false,
        'export-checkbox-review-created': false,
      });
    const fetchUsers= async () => {
        const root_url = process.env.REACT_API_HOST;
        const exportfetchUrl:string = `${root_url}/user-service/api/v1/account/users`;
        await axiosInstance
          .get(exportfetchUrl, {
            headers: {
              Authorization: `Bearer ${loggedInUser.token}`,
              // Add any other headers if needed
            },
          })
          .then((response) => {
            setUserList(response.data);
            console.log("data is", response.data);
          })
          .catch((error) => {
            console.error("Error fetching exports:", error);
          });
    };
    const handleDeleteCheckboxChange = (exportItemId:number) => {
        const updatedCheckboxes = [...selectedDeleteCheckboxes];
        if (updatedCheckboxes.includes(exportItemId)) {
          updatedCheckboxes.splice(updatedCheckboxes.indexOf(exportItemId), 1);//deletes 1 item from the given index
        } else {
          updatedCheckboxes.push(exportItemId);
        }
        setSelectedDeleteCheckboxes(updatedCheckboxes);
      };
    const deleteSelectedExports= async (export_ids:number[]) => {
        const root_url = process.env.REACT_API_HOST;
        
        const exportDeleteURL:string = `${root_url}/user-service/export-app/exports/bulk-delete/`
        await axiosInstance
          .post(exportDeleteURL, {
            export_ids:export_ids
          },{
            headers: {
              Authorization: `Bearer ${loggedInUser.token}`,
              // Add any other headers if needed
            },
          })
          .then((response) => {
            notificationHook.showNotification("Export deleted", {
              type: ToastType.Success,
            });
            setSelectedDeleteCheckboxes([])
            fetchUsers();
          })
          .catch((error) => {
            console.error("Error deleting exports:", error);
            notificationHook.showNotification("Problem deleting exports", {
              type: ToastType.Error,
            });
          });
      // Call your delete API here
    };
    const handleDelete = () => 
    {
        // Implement your delete API call using selectedCheckboxes array
        console.log('Selected Checkboxes:', selectedDeleteCheckboxes);
        if(selectedDeleteCheckboxes.length ==0){
          notificationHook.showNotification('Please select at last one item to be deleted',{
            type: ToastType.Error,
          })
          return;
        }
        deleteSelectedExports(selectedDeleteCheckboxes)
    }
      //use useeffect to call a method right after rendering
  // and also for cleanup
  useEffect(() => {
    if(loggedInUser){
      fetchUsers();
    }
  }, [loggedInUser]);
return (
    <div className="container mt-5">
      <h2 className="mb-4">All Users</h2>
  <table className="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Username</th>
      <th scope="col">Email</th>
      <th scope="col">Type/Role</th>
      <th scope="col">Permission Groups</th>
      <th scope="col">Edit</th>
      <th scope="col">Select</th>
    </tr>
  </thead>
  <tbody>
  {
  userList.map((user) => (
    <tr key={user.id}>
      <th scope="row">{user.id}</th>
      <td>{user.username}</td>
      <td>{user.email}</td>
      <td>{user.role}</td>
      <td>Groups</td>
      <td>
      <Link to="userlist">
        {user.email}
      </Link>
      </td>
      <td><input type="checkbox" className="form-check-input" onChange={() => handleDeleteCheckboxChange(user.id)}/></td>
    </tr>
  ))
}

  </tbody>
</table>
<button className="btn btn-danger" onClick={handleDelete}>Delete</button>

    </div>
  );
};
export default UserList;
