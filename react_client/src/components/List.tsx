import React, { FC } from "react";
import { useAppSelector } from "../store/store";

const List: FC = () => {
  const persons = useAppSelector((state) => state.person.persons);

  return (
    <div>
      <p>This is a list component</p>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {persons.map((person) => (
            <tr key={person.id}>
              <td>{person.id}</td>
              <td>{person.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default List;
