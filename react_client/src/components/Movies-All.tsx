import React from 'react';
import 'styles/movies-list.css'
interface Movie {
  id: number;
  title: string;
  releaseYear: number;
}

const MovieList: React.FC = () => {
  return (
    <>
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
                <div className="candidate-list-box card mt-4">
                  <div className="p-4 card-body">
                    <div className="align-items-center row">
                      <div className="col-auto">
                        <div className="candidate-list-images">
                          <a href="#">
                            <img
                              src="https://bootdey.com/img/Content/avatar/avatar8.png"
                              alt=""
                              className="avatar-md img-thumbnail rounded-circle"
                            />
                          </a>
                        </div>
                      </div>
                      <div className="col-lg-5">
                        <div className="candidate-list-content mt-3 mt-lg-0">
                          <h5 className="fs-19 mb-0">
                            <a className="primary-link" href="#">
                              MichaeL Drake{' '}
                            </a>
                            <span className="badge bg-warning ms-1">
                              <i className="mdi mdi-star align-middle"></i>3.9
                            </span>
                          </h5>
                          <p className="text-muted mb-2">
                            Full Stack Engineer
                          </p>
                          <ul className="list-inline mb-0 text-muted">
                            <li className="list-inline-item">
                              <i className="mdi mdi-map-marker"></i> Oakridge Lane
                              Richardson
                            </li>
                            <li className="list-inline-item">
                              <i className="mdi mdi-wallet"></i> $240 / hours
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div className="col-lg-4">
                        <div className="mt-2 mt-lg-0 d-flex flex-wrap align-items-start gap-1">
                          <span className="badge bg-soft-secondary fs-14 mt-1">
                            Trainer
                          </span>
                          <span className="badge bg-soft-secondary fs-14 mt-1">
                            Adobe illustrator
                          </span>
                        </div>
                      </div>
                    </div>
                    <div className="favorite-icon">
                      <a href="#">
                        <i className="mdi mdi-heart fs-18"></i>
                      </a>
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
    </>
  );
};

export default MovieList;
