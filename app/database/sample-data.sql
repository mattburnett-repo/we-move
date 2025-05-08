-- Insert users
INSERT INTO users (email, password_hash, name) VALUES
('diana@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', 'Diana Prince'),
('eric@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', 'Eric Adams'),
('fiona@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', 'Fiona Gallagher'),
('george@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'George Bailey'),
('hannah@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210', 'Hannah Smith'),
('ian@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef', 'Ian Wright');


-- Insert campaigns
INSERT INTO campaigns (user_id, title, description, goal_amount, current_amount, is_active) VALUES
(1, 'Solar Power for Schools', 'Bringing clean energy to rural classrooms.', 8000, 2500, 1),
(2, 'Neighborhood Food Bank', 'Helping families get nutritious food every week.', 6000, 6000, 0),
(3, 'Animal Shelter Expansion', 'Building new kennels and improving facilities.', 7000, 1750, 1);

-- Insert donations
INSERT INTO donations (campaign_id, donor_id, amount) VALUES
(1, 1, 1000),
(1, 2, 1500),
(2, 3, 4000),
(2, 4, 2000),
(3, 5, 750),
(3, 6, 1000);
