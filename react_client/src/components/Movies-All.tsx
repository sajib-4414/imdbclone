import React, { useEffect, useState } from 'react';
// import 'styles/movies-list.css'
import 'styles/nested-unresolved.css'
import styled from '@emotion/styled';
import axios from 'axios';
interface Movie {
  id: number;
  platform:string;
  storyline:string;
  avg_rating:number;
  number_rating:number;
  title: string;
  releaseYear: number;
}

const MovieList: React.FC = () => {
  const [currentPageMovies, setCurrentPageMovies] = useState<Movie[]>([])
  //use useeffect to call a method right after rendering
  // and also for cleanup
  useEffect(()=>{
    const fetchMovies = async()=>{
      try{
        const root_url =  process.env.REACT_API_HOST
	      const moviesUrl = `${root_url}/movie-service/api/v1/movies`;
        const response = await axios.get(moviesUrl);
        setCurrentPageMovies(response.data);
        // console.log(response.data)
      }catch(error){
        console.error('Error fetching movies:', error);
      }
    }
    fetchMovies();
  },[])

  return (
    <CSSContainer>
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.3.45/css/materialdesignicons.css"
        integrity="sha256-NAxhqDvtY0l4xn+YVa6WjAcmd94NNfttjNsDmNatFVc="
        crossOrigin="anonymous"
      />
      <section className="section">
        <div className="container">
          <div className="justify-content-center row">
            <div className="col-lg-12">
              <div className="candidate-list-widgets mb-4">
                <form action="#" className="">
                  <div className="g-2 row">
                    <div className="col-lg-3">
                      <div className="filler-job-form">
                        <i className="uil uil-briefcase-alt"></i>
                        <input
                          id="exampleFormControlInput1"
                          placeholder="Movie name or actor name"
                          type="search"
                          className="form-control filler-job-input-box form-control"
                        />
                      </div>
                    </div>
                    <div className="col-lg-3">
                      <div className="filler-job-form">
                        <i className="uil uil-location-point"></i>
                        <select
                          className="form-select selectForm__inner"
                          data-trigger="true"
                          name="choices-single-location"
                          id="choices-single-location"
                          aria-label="Default select example"
                        >
                          <option value="AF">Action</option>
                          <option value="AX">Comedy</option>
                          <option value="AL">Horror</option>
                        </select>
                      </div>
                    </div>
                    <div className="col-lg-3">
                      <div className="filler-job-form">
                        <i className="uil uil-clipboard-notes"></i>
                        <select
                          className="form-select selectForm__inner"
                          data-trigger="true"
                          name="choices-single-categories"
                          id="choices-single-categories"
                          aria-label="Default select example"
                        >
                          <option value="4">Hollywood</option>
                          <option value="1">Bollywood</option>
                          <option value="3">Korean</option>
                          <option value="5">Chinese</option>
                        </select>
                      </div>
                    </div>
                    <div className="col-lg-3">
                      <div>
                        <a className="btn btn-primary" href="#">
                          <i className="uil uil-filter"></i> Filter
                        </a>
                        <a className="btn btn-success ms-2" href="#">
                          <i className="uil uil-cog"></i> Advance filter
                        </a>
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div className="row">
            <div className="col-lg-12">
              <div className="align-items-center row">
                <div className="col-lg-8">
                  <div className="mb-3 mb-lg-0">
                    <h6 className="fs-16 mb-0">Showing 1 – 8 of 11 results</h6>
                  </div>
                </div>
                <div className="col-lg-4">
                  <div className="candidate-list-widgets">
                    <div className="row">
                      <div className="col-lg-6">
                        <div className="selection-widget">
                          <select
                            className="form-select"
                            data-trigger="true"
                            name="choices-single-filter-orderby"
                            id="choices-single-filter-orderby"
                            aria-label="Default select example"
                          >
                            <option value="df">Default</option>
                            <option value="ne">Newest</option>
                            <option value="od">Oldest</option>
                            <option value="rd">Random</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-lg-6">
                        <div className="selection-widget mt-2 mt-lg-0">
                          <select
                            className="form-select"
                            data-trigger="true"
                            name="choices-candidate-page"
                            id="choices-candidate-page"
                            aria-label="Default select example"
                          >
                            <option value="df">All</option>
                            <option value="ne">8 per Page</option>
                            <option value="ne">12 per Page</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="candidate-list">
                {currentPageMovies.map((movie)=>(
                  <div className="candidate-list-box card mt-4" key={movie.id}>
                  <div className="p-4 card-body">
                      <div className="align-items-center row">
                          <div className="col-auto">
                              <div className="candidate-list-images">
                                  <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                              </div>
                          </div>
                          <div className="col-lg-5">
                              <div className="candidate-list-content mt-3 mt-lg-0">
                                  <h5 className="fs-19 mb-0">
                                      <a className="primary-link" href="#">{movie.title}</a>
                                      {/* {movie.avg_rating>4?yes:no}
                                      <span className="badge bg-success ms-1">
                                        <i className="mdi mdi-star align-middle">
                                          </i>{movie.avg_rating}
                                      </span> */}
                                      <RatingBadge movie={movie}/>
                                  </h5>
                                  <p className="text-muted mb-2">Platform:{movie.platform}</p>
                                  <ul className="list-inline mb-0 text-muted">
                                      <li className="list-inline-item">2022</li>
                                      <li className="list-inline-item"><i className="mdi mdi-clock"></i> 2h 22min</li>
                                  </ul>
                              </div>
                          </div>
                          <div className="col-lg-4">
                              <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1">
                                  <span className="badge bg-soft-secondary fs-14 mt-1">Genre1</span><span className="badge bg-soft-secondary fs-14 mt-1">Genre2</span><span className="badge bg-soft-secondary fs-14 mt-1">Genre3</span>
                              </div>
                          </div>
                      </div>
                      <div className="favorite-icon">
                           <a href="#"><span>Rate</span> <i className="mdi mdi-star fs-18"></i></a>
                      </div>
                      
                  </div>
              </div>
                ))}
              <div className="candidate-list-box card mt-4">
                        <div className="p-4 card-body">
                            <div className="align-items-center row">
                                <div className="col-auto">
                                    <div className="candidate-list-images">
                                        <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                                    </div>
                                </div>
                                <div className="col-lg-5">
                                    <div className="candidate-list-content mt-3 mt-lg-0">
                                        <h5 className="fs-19 mb-0">
                                            <a className="primary-link" href="#">Charles Dickens</a><span className="badge bg-success ms-1"><i className="mdi mdi-star align-middle"></i>4.8</span>
                                        </h5>
                                        <p className="text-muted mb-2">Project Manager</p>
                                        <ul className="list-inline mb-0 text-muted">
                                            <li className="list-inline-item"><i className="mdi mdi-map-marker"></i> Oakridge Lane Richardson</li>
                                            <li className="list-inline-item"><i className="mdi mdi-wallet"></i> $650 / hours</li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4">
                                    <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1">
                                        <span className="badge bg-soft-secondary fs-14 mt-1">Leader</span><span className="badge bg-soft-secondary fs-14 mt-1">Manager</span><span className="badge bg-soft-secondary fs-14 mt-1">Developer</span>
                                    </div>
                                </div>
                            </div>
                            <div className="favorite-icon">
                                <a href="#"><i className="mdi mdi-heart fs-18"></i></a>
                            </div>
                        </div>
                    </div>
                    <div className="candidate-list-box bookmark-post card mt-4">
                        <div className="p-4 card-body">
                            <div className="align-items-center row">
                                <div className="col-auto">
                                    <div className="candidate-list-images">
                                        <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar2.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                                    </div>
                                </div>
                                <div className="col-lg-5">
                                    <div className="candidate-list-content mt-3 mt-lg-0">
                                        <h5 className="fs-19 mb-0">
                                            <a className="primary-link" href="#">Gabriel Palmer</a>
                                            <span className="badge bg-warning ms-1">
                                              <i className="mdi mdi-star align-middle">
                                                </i>3.4
                                                </span>
                                        </h5>
                                        <p className="text-muted mb-2">HTML Developer</p>
                                        <ul className="list-inline mb-0 text-muted">
                                            <li className="list-inline-item"><i className="mdi mdi-map-marker"></i> Oakridge Lane California</li>
                                            <li className="list-inline-item"><i className="mdi mdi-wallet"></i> $250 / hours</li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4">
                                    <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1"><span className="badge bg-soft-secondary fs-14 mt-1">Design</span><span className="badge bg-soft-secondary fs-14 mt-1">Developer</span></div>
                                </div>
                            </div>
                            <div className="favorite-icon">
                                <a href="#"><i className="mdi mdi-heart fs-18"></i></a>
                            </div>
                        </div>
                    </div>
                    <div className="candidate-list-box card mt-4">
                        <div className="p-4 card-body">
                            <div className="align-items-center row">
                                <div className="col-auto">
                                    <div className="candidate-list-images">
                                        <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar3.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                                    </div>
                                </div>
                                <div className="col-lg-5">
                                    <div className="candidate-list-content mt-3 mt-lg-0">
                                        <h5 className="fs-19 mb-0">
                                            <a className="primary-link" href="#">Rebecca Swartz </a>
                                            <span className="badge bg-success ms-1">
                                              <i className="mdi mdi-star align-middle">
                                                </i>4.3
                                                </span>
                                        </h5>
                                        <p className="text-muted mb-2">Graphic Designer</p>
                                        <ul className="list-inline mb-0 text-muted">
                                            <li className="list-inline-item"><i className="mdi mdi-map-marker"></i> Oakridge Lane Richardson</li>
                                            <li className="list-inline-item"><i className="mdi mdi-wallet"></i> $380 / hours</li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4">
                                    <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1"><span className="badge bg-soft-secondary fs-14 mt-1">Design</span><span className="badge bg-soft-secondary fs-14 mt-1">Developer</span></div>
                                </div>
                            </div>
                            <div className="favorite-icon">
                                <a href="#"><i className="mdi mdi-heart fs-18"></i></a>
                            </div>
                        </div>
                    </div>
                    <div className="candidate-list-box bookmark-post card mt-4">
                        <div className="p-4 card-body">
                            <div className="align-items-center row">
                                <div className="col-auto">
                                    <div className="candidate-list-images">
                                        <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar4.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                                    </div>
                                </div>
                                <div className="col-lg-5">
                                    <div className="candidate-list-content mt-3 mt-lg-0">
                                        <h5 className="fs-19 mb-0">
                                            <a className="primary-link" href="#">Betty Richards</a><span className="badge bg-success ms-1"><i className="mdi mdi-star align-middle"></i>4.5</span>
                                        </h5>
                                        <p className="text-muted mb-2">Education Training</p>
                                        <ul className="list-inline mb-0 text-muted">
                                            <li className="list-inline-item"><i className="mdi mdi-map-marker"></i> Oakridge Lane Richardson</li>
                                            <li className="list-inline-item"><i className="mdi mdi-wallet"></i> $650 / hours</li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4">
                                    <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1">
                                        <span className="badge bg-soft-secondary fs-14 mt-1">Trainer</span><span className="badge bg-soft-secondary fs-14 mt-1">Adobe illustrator</span>
                                    </div>
                                </div>
                            </div>
                            <div className="favorite-icon">
                                <a href="#"><i className="mdi mdi-heart fs-18"></i></a>
                            </div>
                        </div>
                    </div>
                    <div className="candidate-list-box card mt-4">
                        <div className="p-4 card-body">
                            <div className="align-items-center row">
                                <div className="col-auto">
                                    <div className="candidate-list-images">
                                        <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar5.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                                    </div>
                                </div>
                                <div className="col-lg-5">
                                    <div className="candidate-list-content mt-3 mt-lg-0">
                                        <h5 className="fs-19 mb-0">
                                            <a className="primary-link" href="#">Jeffrey Montgomery</a><span className="badge bg-success ms-1"><i className="mdi mdi-star align-middle"></i>4.9</span>
                                        </h5>
                                        <p className="text-muted mb-2">Restaurant Team Member</p>
                                        <ul className="list-inline mb-0 text-muted">
                                            <li className="list-inline-item"><i className="mdi mdi-map-marker"></i> Oakridge Lane Richardson</li>
                                            <li className="list-inline-item"><i className="mdi mdi-wallet"></i> $125 / hours</li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4">
                                    <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1">
                                        <span className="badge bg-soft-secondary fs-14 mt-1">Trainer</span><span className="badge bg-soft-secondary fs-14 mt-1">Adobe illustrator</span>
                                    </div>
                                </div>
                            </div>
                            <div className="favorite-icon">
                                <a href="#"><i className="mdi mdi-heart fs-18"></i></a>
                            </div>
                        </div>
                    </div>
                    <div className="candidate-list-box card mt-4">
                        <div className="p-4 card-body">
                            <div className="align-items-center row">
                                <div className="col-auto">
                                    <div className="candidate-list-images">
                                        <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar6.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                                    </div>
                                </div>
                                <div className="col-lg-5">
                                    <div className="candidate-list-content mt-3 mt-lg-0">
                                        <h5 className="fs-19 mb-0">
                                            <a className="primary-link" href="#">Milton Osborn</a><span className="badge bg-danger ms-1"><i className="mdi mdi-star align-middle"></i>2.5</span>
                                        </h5>
                                        <p className="text-muted mb-2">Assistant / Store Keeper</p>
                                        <ul className="list-inline mb-0 text-muted">
                                            <li className="list-inline-item"><i className="mdi mdi-map-marker"></i> Oakridge Lane Richardson</li>
                                            <li className="list-inline-item"><i className="mdi mdi-wallet"></i> $455 / hours</li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4">
                                    <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1">
                                        <span className="badge bg-soft-secondary fs-14 mt-1">Trainer</span><span className="badge bg-soft-secondary fs-14 mt-1">Adobe illustrator</span>
                                    </div>
                                </div>
                            </div>
                            <div className="favorite-icon">
                                <a href="#"><i className="mdi mdi-heart fs-18"></i></a>
                            </div>
                        </div>
                    </div>
                    <div className="candidate-list-box card mt-4">
                        <div className="p-4 card-body">
                            <div className="align-items-center row">
                                <div className="col-auto">
                                    <div className="candidate-list-images">
                                        <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                                    </div>
                                </div>
                                <div className="col-lg-5">
                                    <div className="candidate-list-content mt-3 mt-lg-0">
                                        <h5 className="fs-19 mb-0">
                                            <a className="primary-link" href="#">Harold Jordan</a><span className="badge bg-success ms-1"><i className="mdi mdi-star align-middle"></i>4.9</span>
                                        </h5>
                                        <p className="text-muted mb-2">Executive, HR Operations</p>
                                        <ul className="list-inline mb-0 text-muted">
                                            <li className="list-inline-item"><i className="mdi mdi-map-marker"></i> Oakridge Lane Richardson</li>
                                            <li className="list-inline-item"><i className="mdi mdi-wallet"></i> $799 / hours</li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4">
                                    <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1">
                                        <span className="badge bg-soft-secondary fs-14 mt-1">Trainer</span><span className="badge bg-soft-secondary fs-14 mt-1">Adobe illustrator</span>
                                    </div>
                                </div>
                            </div>
                            <div className="favorite-icon">
                                <a href="#"><i className="mdi mdi-heart fs-18"></i></a>
                            </div>
                        </div>
                    </div>
                    <div className="candidate-list-box card mt-4">
                        <div className="p-4 card-body">
                            <div className="align-items-center row">
                                <div className="col-auto">
                                    <div className="candidate-list-images">
                                        <a href="#"><img src="https://bootdey.com/img/Content/avatar/avatar8.png" alt="" className="avatar-md img-thumbnail rounded-circle" /></a>
                                    </div>
                                </div>
                                <div className="col-lg-5">
                                    <div className="candidate-list-content mt-3 mt-lg-0">
                                        <h5 className="fs-19 mb-0">
                                            <a className="primary-link" href="#">MichaeL Drake </a><span className="badge bg-warning ms-1"><i className="mdi mdi-star align-middle"></i>3.9</span>
                                        </h5>
                                        <p className="text-muted mb-2">Full Stack Engineer</p>
                                        <ul className="list-inline mb-0 text-muted">
                                            <li className="list-inline-item"><i className="mdi mdi-map-marker"></i> Oakridge Lane Richardson</li>
                                            <li className="list-inline-item"><i className="mdi mdi-wallet"></i> $240 / hours</li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4">
                                    <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1">
                                        <span className="badge bg-soft-secondary fs-14 mt-1">Trainer</span><span className="badge bg-soft-secondary fs-14 mt-1">Adobe illustrator</span>
                                    </div>
                                </div>
                            </div>
                            <div className="favorite-icon">
                                <a href="#"><i className="mdi mdi-heart fs-18"></i></a>
                            </div>
                        </div>
                    </div>

              </div>
            </div>
          </div>
          <div className="row">
            <div className="mt-4 pt-2 col-lg-12">
              <nav aria-label="Page navigation example">
                <div className="pagination job-pagination mb-0 justify-content-center">
                  <li className="page-item disabled">
                    <a className="page-link" tabIndex={-1} href="#">
                      <i className="mdi mdi-chevron-double-left fs-15"></i>
                    </a>
                  </li>
                  <li className="page-item active">
                    <a className="page-link" href="#">
                      1
                    </a>
                  </li>
                  <li className="page-item">
                    <a className="page-link" href="#">
                      2
                    </a>
                  </li>
                  <li className="page-item">
                    <a className="page-link" href="#">
                      3
                    </a>
                  </li>
                  <li className="page-item">
                    <a className="page-link" href="#">
                      4
                    </a>
                  </li>
                  <li className="page-item">
                    <a className="page-link" href="#">
                      <i className="mdi mdi-chevron-double-right fs-15"></i>
                    </a>
                  </li>
                </div>
              </nav>
            </div>
          </div>
        </div>
      </section>
    </CSSContainer>
  );
};

const StyledContainer = styled.div`
.card {
  box-shadow: 0 20px 27px 0 rgb(0 0 0 / 5%);
}
.avatar-md {
  height: 5rem;
  width: 5rem;
}
.fs-19 {
  font-size: 19px;
}
.primary-link {
  color: #314047;
  -webkit-transition: all .5s ease;
  transition: all .5s ease;
}

.fs-14 {
  font-size: 14px;
}

.bg-soft-secondary {
  background-color: rgba(116,120,141,.15)!important;
  color: #74788d!important;
}

.mt-1 {
  margin-top: 0.25rem!important;
}
`;

interface CSSContainerProps {
  children?: React.ReactNode;
}

const CSSContainer: React.FC<CSSContainerProps> = ({ children }) => {
  return <StyledContainer>{children}</StyledContainer>;
};

interface RatingBadgeProps {
  movie: { avg_rating: number; title: string };
}
const RatingBadge:React.FC<RatingBadgeProps> = ({movie})=>{
  const getBadgeClass = () => {
    if (movie.avg_rating > 4) {
      return 'badge bg-success ms-1';
    } else if (movie.avg_rating < 2) {
      return 'badge bg-danger ms-1';
    } else {
      return 'badge bg-warning ms-1';
    }
  };
  return (
    <span className={getBadgeClass()}>
        <i className="mdi mdi-star align-middle"></i>
        {movie.avg_rating}
    </span>
  );
}


export default MovieList;
