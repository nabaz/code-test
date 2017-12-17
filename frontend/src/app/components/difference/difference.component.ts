import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Validators, FormControl, FormGroup, FormBuilder } from '@angular/forms';
import {Http} from '@angular/http';
import 'rxjs/Rx';
import { Difference } from '../../models/difference';
import {Observable} from "rxjs/Observable";

@Component({
  selector: 'app-difference',
  templateUrl: './difference.component.html',
  styleUrls: ['./difference.component.css'],
  providers: [ApiService]


})
export class DifferenceComponent {
  result: string;
  differences: Difference[];

  newNumber: FormControl;
  addNewForm: FormGroup;
  constructor(http: Http, private _dj: ApiService, private fb:FormBuilder){
    this._dj.getDifference()
    .subscribe(result => {
        this.result = result
    });
  }
  ngOnInit() {
      this.addNewForm = new FormGroup({
          'value': new FormControl(this.newNumber, [
            Validators.required,
            Validators.maxLength(100),
          ]),
      })
      this._dj.getDifference()
      .subscribe(differences => this.differences = differences);

  }
  add() {
      let data = this.addNewForm.value
      this._dj.createDifference(data).subscribe(
        data => {
          this._dj.getDifference();
          this.differences.push(data);
          return "value added";
        },
        error => {
          console.error("Error Saving Data");
        }
      )


  }
}
