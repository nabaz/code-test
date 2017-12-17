import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import  { Http } from '@angular/http';
import { ApiService } from './services/api.service';
import {HttpModule} from '@angular/http';
import { AppComponent }  from './app.component';
import { DifferenceComponent }  from './components/difference/difference.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CustomFormsModule } from 'ng2-validation';

import { routing } from './app.routes';


@NgModule({
imports: [
      BrowserModule,
      HttpModule,
      BrowserModule,
      FormsModule,
      CustomFormsModule,
      ReactiveFormsModule,
      routing
  ],
  declarations: [ AppComponent, DifferenceComponent ],
  bootstrap:    [ AppComponent],
  providers:    [ ApiService, HttpModule ]

})
export class AppModule { }
