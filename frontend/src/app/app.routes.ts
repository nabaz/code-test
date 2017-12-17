// ====== ./app/app.routes.ts ======

// Imports
// Deprecated import
import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DifferenceComponent }  from './components/difference/difference.component';

// Route Configuration
export const routes: Routes = [
    { path: 'differences', component: DifferenceComponent },
];

// Deprecated provide
// export const APP_ROUTER_PROVIDERS = [
//   provideRouter(routes)
// ];

export const routing: ModuleWithProviders = RouterModule.forRoot(routes);
