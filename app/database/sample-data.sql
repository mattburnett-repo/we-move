-- Insert users
INSERT INTO users (email, password_hash, name) VALUES
('diana@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', 'Diana Prince'),
('eric@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', 'Eric Adams'),
('fiona@example.com', 'pbkdf2:sha256:50000$XYZ1QweT$1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', 'Fiona Gallagher');

-- Insert campaigns
INSERT INTO campaigns (user_id, title, description, goal_amount, current_amount, is_active) VALUES
(1, 'Solar Power for Schools', 'Bringing clean energy to rural classrooms.', 8000, 2500, 1),
(2, 'Neighborhood Food Bank', 'Helping families get nutritious food every week.', 6000, 6000, 0),
(3, 'Animal Shelter Expansion', 'Building new kennels and improving facilities.', 7000, 1750, 1);

-- Insert donations
INSERT INTO donations (campaign_id, donor_name, amount) VALUES
(1, 'Clark Kent', 1000),
(1, 'Lois Lane', 1500),
(2, 'Bruce Wayne', 4000),
(2, 'Selina Kyle', 2000),
(3, 'Barry Allen', 750),
(3, 'Iris West', 1000);
