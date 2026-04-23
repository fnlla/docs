# Routing

FNLLA routing supports named routes, middleware groups, and signed URL generation.

```php
Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
```
