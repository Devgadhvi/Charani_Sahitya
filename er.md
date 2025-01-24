```mermaid
erDiagram
erDiagram
    User ||--o{ Comment : "makes"
    User ||--o{ Rating : "gives"
    User {
        int id PK
        string username
        string email
        string password
        datetime date_joined
        boolean is_active
    }

    Author ||--o{ Song : "writes"
    Author ||--o{ Book : "writes"
    Author ||--o{ Story : "writes"
    Author {
        int id PK
        string name
        text biography
        date birth_date
        date death_date
        string region
        datetime created_at
    }

    Category ||--o{ Song : "contains"
    Category ||--o{ Book : "contains"
    Category ||--o{ Story : "contains"
    Category {
        int id PK
        string name
        text description
        string slug
    }

    Song ||--o{ Comment : "receives"
    Song ||--o{ Rating : "receives"
    Song {
        int id PK
        string title
        text content
        int author_id FK
        int category_id FK
        string region
        string language
        string audio_file
        text lyrics
        text translation
        int views
        datetime created_at
        datetime updated_at
    }

    Book ||--o{ Comment : "receives"
    Book ||--o{ Rating : "receives"
    Book {
        int id PK
        string title
        int author_id FK
        text description
        date publication_date
        string pdf_file
        string cover_image
        int category_id FK
        string language
        int views
        datetime created_at
    }

    Story ||--o{ Comment : "receives"
    Story ||--o{ Rating : "receives"
    Story {
        int id PK
        string title
        text content
        int author_id FK
        int category_id FK
        string region
        int views
        datetime created_at
        datetime updated_at
    }

    Comment {
        int id PK
        int user_id FK
        text content
        datetime created_at
        int content_type_id
        int object_id
    }

    Rating {
        int id PK
        int user_id FK
        int value
        datetime created_at
        int content_type_id
        int object_id
    }