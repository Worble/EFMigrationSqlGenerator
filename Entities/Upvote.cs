namespace MigrationGenerator.Entities
{
    public class Upvote : BaseEntity
    {
        public User User { get; set; }
        public Post Post { get; set; }
    }
}