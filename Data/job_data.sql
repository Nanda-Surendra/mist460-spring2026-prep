CREATE TABLE Job (
    JobID           INT IDENTITY(1,1) CONSTRAINT PK_Job PRIMARY KEY,
    JobTitle  NVARCHAR(MAX) NOT NULL,
    Industry        NVARCHAR(100) NULL,
	JobDescription NVARCHAR(MAX) NULL
);


INSERT INTO Job (JobTitle, Industry, JobDescription) VALUES
(N'Agentic Engineer', N'Technology', N'Agentic Engineers design, build, and maintain autonomous AI systems that can perform complex tasks with minimal human intervention. They develop AI agents capable of learning, reasoning, and decision-making across various domains. Responsibilities include designing agent architectures, implementing machine learning algorithms, ensuring ethical AI behavior, and integrating agents into real-world applications. Agentic Engineers work on cutting-edge technologies to create intelligent systems that can operate independently while adhering to safety and ethical standards.'),
 (N'Software Engineer', N'Technology', N'Software Engineers design, develop, test, and maintain software applications and systems. They write clean, efficient code, collaborate with cross-functional teams, participate in code reviews, and solve complex technical problems while following best practices in software development, version control, and agile methodologies.'),
 (N'Business Systems Analyst', N'Consulting', N'Business Systems Analysts bridge the gap between business needs and technology solutions by gathering requirements, analyzing processes, and recommending system improvements. They work with stakeholders to document workflows, create specifications, and ensure IT solutions align with organizational objectives and deliver measurable business value.'),
 (N'Cybersecurity Analyst', N'Cybersecurity', N'Cybersecurity Analysts protect organizations from cyber threats by monitoring networks for security breaches, investigating incidents, implementing security measures, and conducting vulnerability assessments. They analyze security logs, respond to incidents, develop security policies, and stay current with emerging threats and defense technologies.'),
 (N'Product Manager',   N'Technology', N'Product Managers define product vision and strategy, prioritize features, and guide development teams to create successful products. They conduct market research, gather user feedback, create roadmaps, make data-driven decisions, and coordinate with engineering, design, and marketing teams to deliver products that meet customer needs and business goals.'),
 (N'Database Administrator', N'Technology', N'Database Administrators ensure the performance, security, and availability of organizational databases. They install and configure database systems, perform backups and recovery, optimize queries, manage user access, monitor performance metrics, and implement security measures to protect sensitive data while maintaining system reliability.');
