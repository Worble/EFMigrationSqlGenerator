# Why?
Writing SQL is lame so I bully EF into doing it for me, and I steal it's lunch money while it's at it.

In all seriousness, making entity relationships in C# and using EF to scaffold migrations is 100% quicker (at least for me) than writing all tables and columns manually, so that's why this exists. The current use-case is using it to generate the sql for migrations handled by diesel-cli in a different rust project.

It also allows me to develop in SQLite and Deploy in Postgres, since EF handles the differences in the two schema.

# Usage
Run `python generate_sql.py` in your project root that has Entity Framework configured (this may take some time dependant on the amount of migrations). This will generate a folder called "sql" with your migrations inside. The rest of this repo is just an example project of how it is used and what it generates.

The SQL generated will be specific to the database configured in EF, to change this, find where you specify the database connection for EF (in this project that is the `OnConfiguring` method in BoardContext.cs) and change Options Builder to use your preferred database. For example, in this project change `optionsBuilder.UseNpgsql("Server=127.0.0.1;Port=5433;Database=Boards;User Id=postgres;Password=postgres;");` to `optionsBuilder.UseSqlite("Data Source=boards.db");`, remove the sql folder if it exists, and regenerate the SQL (Note that the specified database, or even database connection doesn't need to exist, as we are not actually performing the migrations). The resulting code will no longer use postgres specific schema (such as the `SERIAL` type for primary keys), and will also highlight why SQLite is not a good choice for migrations.

The SQL generated will also be restrained by the type of Database as well; EF will throw an error if a migration modifies a column when it's set to SQLite for example, since SQLite cannot edit table columns, so you will need to either reset your migrations in EF to fix this problem, or write the SQL yourself to copy the data and create a new table. All other valid migrations will still be made, so be sure to check the stderr output (as well as the SQL!) before blindly using the generated SQL. 