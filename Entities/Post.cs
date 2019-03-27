using System.Collections.Generic;

namespace MigrationGenerator.Entities
{
    public class Post : BaseEntity
    {
        public string Title { get; set; }
        public string Content { get; set; }
        public User Owner { get; set; }
        public string Topic { get; set; }
    }
}