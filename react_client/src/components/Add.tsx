import React, { FC, useRef } from 'react';
import { addPerson, savePerson } from '../store/features/personSlice';
import { useAppDispatch } from '../store/store';

const Add: FC = () => {
  const name = useRef<string>("");
  const dispatch = useAppDispatch();

  return (
    <form className="mt-3">
      <div className="mb-3">
        <label htmlFor="personName" className="form-label">
          Person Name:
        </label>
        <input
          type="text"
          className="form-control"
          id="personName"
          onChange={(e) => (name.current = e.target.value)}
        />
      </div>
      <button
        type="button"
        className="btn btn-primary"
        onClick={() => dispatch(savePerson( name.current ))}
      >
        Add
      </button>
    </form>
  );
};

export default Add;
