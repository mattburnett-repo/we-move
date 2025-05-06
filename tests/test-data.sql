-- Insert users
INSERT INTO users (email, password_hash, name) VALUES
('alice@example.com', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f', 'Alice Walker'),
('bob@example.com', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f', 'Bob Smith'),
('carla@example.com', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f', 'Carla Johnson');

-- Insert campaigns
INSERT INTO campaigns (user_id, title, description, goal_amount, current_amount, is_active) VALUES
(1, 'Clean Water for All', 'Raising funds to build wells in underserved areas.', 5000, 1250, 1),
(2, 'Books for Kids', 'A campaign to provide books for underfunded schools.', 3000, 3000, 0),
(1, 'Community Garden Project', 'Turning vacant lots into gardens.', 4000, 1100, 1);

-- Insert donations
INSERT INTO donations (campaign_id, donor_name, amount) VALUES
(1, 'John Doe', 250),
(1, 'Jane Smith', 500),
(1, 'Anonymous', 500),
(2, 'Emily Chen', 1000),
(2, 'Anonymous', 2000),
(3, 'Tom Lee', 300),
(3, 'Dana Patel', 800);
