import React, {useState} from 'react'
import Error from '../../common/Error';

const Signup:React.FC =()=>{
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        username: '',
        password: '',
        confirmPassword: '',
      });
      const [signupErrors, setSignUpErrors] = useState([]);

      const signUpvalidate = ():boolean =>{
        const errors = []
        switch(true){
            case formData['password'] !== formData['confirmPassword']:
                errors.push({
                    "error_code":"password_not_match",
                    "error_details":"Passwords does not match"
                })
        }
        setSignUpErrors(errors)
        if(errors.length>0) return false
        else return true
    }
    
      const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({
          ...formData,
          [e.target.name]: e.target.value,
        });
      };
      const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if(!signUpvalidate()) return;
        
        // Add your signup logic here using the form data
        console.log('Form submitted:', formData);
      };
      return(
        <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <h2 className="mb-4">Sign Up</h2>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="name" className="form-label">
                Name
              </label>
              <input
                type="text"
                className="form-control"
                id="name"
                placeholder="Enter your name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="email" className="form-label">
                Email
              </label>
              <input
                type="email"
                className="form-control"
                id="email"
                placeholder="Enter your email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="username" className="form-label">
                Username
              </label>
              <input
                type="text"
                className="form-control"
                id="username"
                placeholder="Choose a username"
                name="username"
                value={formData.username}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="password" className="form-label">
                Password
              </label>
              <input
                type="password"
                className="form-control"
                id="password"
                placeholder="Enter your password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="confirmPassword" className="form-label">
                Confirm Password
              </label>
              <input
                type="password"
                className="form-control"
                id="confirmPassword"
                placeholder="Confirm your password"
                name="confirmPassword"
                value={formData.confirmPassword}
                onChange={handleChange}
                required
              />
            </div>

            <button type="submit" className="btn btn-primary">
              Sign Up
            </button>
          </form>
          {signupErrors.length > 0 && <Error errors={signupErrors} />}
        </div>
      </div>
    </div>
  );
}
export default Signup;