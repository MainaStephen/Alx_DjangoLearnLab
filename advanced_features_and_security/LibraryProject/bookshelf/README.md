## 🔐 Permissions and Groups Setup

### Custom Permissions (in `Book` model):
- `can_view`: View book listings
- `can_create`: Create new books
- `can_edit`: Edit book records
- `can_delete`: Delete book records

### Groups:
- **Viewers**: Can only view book list
- **Editors**: Can view, create, and edit books
- **Admins**: Full control (view, create, edit, delete)

### How It Works:
- Permissions are enforced using `@permission_required` decorators in views.
- Groups are auto-created with `post_migrate` signal in `accounts/signals.py`.
- Permissions are assigned to groups during the first migration.
