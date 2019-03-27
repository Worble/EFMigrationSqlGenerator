using System.Data.Common;
using Microsoft.EntityFrameworkCore;
using MigrationGenerator.Entities;

namespace MigrationGenerator
{
    public class TestContext : DbContext
    {
        public DbSet<Post> Posts { get; set; }
        public DbSet<User> Users { get; set; }
        public DbSet<Upvote> Upvotes { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            //optionsBuilder.UseSqlite("Data Source=test.db");
            optionsBuilder.UseNpgsql("Server=127.0.0.1;Port=5433;Database=Test;User Id=postgres;Password=postgres;");
        }

    }
}