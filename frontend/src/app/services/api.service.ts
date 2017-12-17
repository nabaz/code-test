import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { Headers, RequestOptions, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import { DifferenceComponent } from '../components/difference/difference.component';
import { Difference } from '../models/difference';


@Injectable()
export class ApiService {
  private apiUrl = 'http://localhost:8000/difference'
  constructor(private http: Http) {}
  getDifference() {
      return this.http.get(this.apiUrl)
          .map(response => response.json())
          .catch(this.handleError)
  }

  createDifference(data: Difference) {
      let headers = new Headers({'Content-Type' : 'application/json'});
      let options = new RequestOptions({ headers: headers });
      let body = JSON.stringify(data);
      return this.http.post(this.apiUrl, body, options).map((res: Response) => res.json());
  }
  private handleError(error: any) {
      console.error('An error occurred', error);
      return Promise.reject(error.message || error);
  }

}
