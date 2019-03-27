using Microsoft.EntityFrameworkCore.Migrations;

namespace MigrationGenerator.Migrations
{
    public partial class addedtopictoposts : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Topic",
                table: "Posts",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Topic",
                table: "Posts");
        }
    }
}
