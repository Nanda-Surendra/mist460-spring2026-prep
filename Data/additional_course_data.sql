-- Another 16 Course rows to make a total of 40 courses for testing purposes

INSERT INTO Course (SubjectCode, CourseNumber, Title, CourseDescription, Credits, Capacity) VALUES

('MIST', '301', 'IT Service Management',
N'This course covers the principles and practices of IT service management using the ITIL framework. Students explore service design, service transition, service operation, and continual service improvement processes. Topics include incident management, problem management, change management, and service level agreements. Students learn to align IT services with business needs, manage service portfolios, and implement service desk operations. Through case studies and simulations, students develop skills in delivering high-quality IT services and managing the complete lifecycle of IT services within organizations.',
3.0, 40),

('MIST', '302', 'Enterprise Architecture',
N'An exploration of enterprise architecture frameworks and their role in aligning business strategy with IT infrastructure. Students study the Zachman Framework, TOGAF, and other architectural approaches for designing cohesive enterprise systems. Topics include business architecture, application architecture, data architecture, and technology architecture. The course covers architecture governance, roadmap development, and managing architectural change. Students analyze real enterprise architecture case studies and develop architectural models for organizations, learning to balance business agility with technical standardization and long-term strategic planning.',
3.0, 35),

('MIST', '410', 'IT Governance and Compliance',
N'This course examines frameworks and practices for governing information technology and ensuring regulatory compliance. Students explore COBIT, ISO 27001, SOX compliance, and industry-specific regulatory requirements. Topics include IT risk management, audit processes, policy development, and compliance monitoring. The course covers data governance, privacy regulations including GDPR and CCPA, and building organizational compliance programs. Students develop governance frameworks and compliance strategies through practical exercises, learning to balance regulatory requirements with operational efficiency while managing IT-related risks in modern organizations.',
3.0, 35),

('CS', '315', 'Software Engineering Principles',
N'A comprehensive study of software engineering methodologies, tools, and best practices for developing large-scale software systems. Students explore software development life cycles, requirements engineering, software architecture, design patterns, and quality assurance. Topics include Agile and Scrum methodologies, continuous integration and deployment, version control, and code review practices. The course emphasizes collaborative development through team projects where students experience the full software engineering process from requirements through deployment. Students develop skills in writing maintainable, testable, and well-documented code for professional software development environments.',
3.0, 35),

('CS', '320', 'Operating Systems',
N'An in-depth study of operating system concepts, design, and implementation. Students explore process management, memory management, file systems, and input/output systems. Topics include CPU scheduling algorithms, deadlock prevention, virtual memory, and concurrency control. The course covers both theoretical foundations and practical aspects of modern operating systems including Linux and Windows architectures. Laboratory work involves programming exercises in process synchronization, memory allocation, and file system implementation. Students gain a deep understanding of how operating systems manage hardware resources and provide services to application software.',
3.0, 30),

('CS', '410', 'Algorithms and Complexity',
N'An advanced study of algorithm design techniques and computational complexity theory. Students explore dynamic programming, greedy algorithms, divide and conquer strategies, graph algorithms, and network flow problems. The course covers NP-completeness, approximation algorithms, and randomized algorithms. Students analyze algorithm correctness and efficiency, applying asymptotic analysis to evaluate performance. Through rigorous problem sets and programming assignments, students develop strong algorithmic thinking and problem-solving skills. The course prepares students for technical interviews, competitive programming, and advanced research in computer science.',
3.0, 30),

('DH', '315', 'Clinical Informatics',
N'This course examines the application of informatics principles within clinical healthcare settings. Students explore clinical decision support systems, electronic health record optimization, clinical workflow analysis, and health data standards including HL7 and FHIR. Topics include medication management systems, computerized physician order entry, nursing informatics, and patient safety technologies. The course covers the role of clinical informaticists in bridging healthcare and information technology. Students analyze clinical information systems and develop strategies for improving clinical workflows, patient safety, and care quality through effective use of health information technologies.',
3.0, 40),

('DH', '350', 'Telehealth and Remote Care',
N'A comprehensive examination of telehealth technologies, policies, and practices transforming healthcare delivery. Students explore synchronous and asynchronous telehealth modalities, remote patient monitoring, virtual care platforms, and mobile health interventions. Topics include telehealth regulatory frameworks, reimbursement policies, technology infrastructure requirements, and patient engagement strategies. The course examines telehealth implementation across specialties including behavioral health, chronic disease management, and acute care. Students analyze telehealth program outcomes and develop implementation plans, gaining practical understanding of how remote care technologies expand healthcare access and improve patient outcomes.',
3.0, 35),

('MKTG', '300', 'Marketing Research Methods',
N'This course provides a systematic introduction to marketing research design, data collection, and analysis. Students learn both qualitative and quantitative research methodologies including surveys, focus groups, observational research, and experimental design. Topics include questionnaire design, sampling strategies, statistical analysis of marketing data, and research report writing. The course emphasizes translating research findings into actionable marketing insights. Students conduct original research projects, applying learned methodologies to real marketing questions. The course develops critical evaluation skills for assessing research quality and interpreting findings to support strategic marketing decisions.',
3.0, 45),

('MKTG', '360', 'Brand Management',
N'An in-depth exploration of brand strategy, development, and management in contemporary markets. Students examine brand identity, brand equity, positioning strategies, and brand architecture decisions. Topics include brand storytelling, visual identity systems, brand extensions, co-branding, and managing brand reputation in digital environments. The course covers global branding challenges, brand revitalization strategies, and measuring brand performance. Through brand audit projects and case analyses of iconic brands, students develop skills in building, managing, and protecting brand assets. The course prepares students for brand management roles in consumer goods, services, and technology companies.',
3.0, 40),

('ENTR', '320', 'Design Thinking and Innovation',
N'This course introduces design thinking as a human-centered approach to innovation and problem solving. Students learn the five stages of design thinking including empathize, define, ideate, prototype, and test through hands-on projects. Topics include user research techniques, journey mapping, rapid prototyping, and iterative testing with end users. The course explores how design thinking applies to product development, service design, organizational change, and social innovation. Students work in multidisciplinary teams to tackle real-world challenges, developing creative confidence and practical skills in applying design thinking methodologies to generate innovative solutions.',
3.0, 45),

('ENTR', '360', 'Venture Finance and Funding',
N'A comprehensive course on financing strategies for new and growing ventures. Students explore bootstrapping, angel investment, venture capital, crowdfunding, and alternative financing mechanisms. Topics include financial modeling for startups, valuation methodologies, term sheet negotiation, and managing investor relationships. The course covers the stages of venture financing from pre-seed through IPO, examining the perspectives of both entrepreneurs and investors. Through financial modeling exercises and pitch preparation, students develop skills in communicating financial narratives, structuring funding rounds, and making strategic financing decisions for early-stage and growth ventures.',
3.0, 35),

('ENTR', '380', 'Global Entrepreneurship',
N'This course examines entrepreneurship in international and cross-cultural contexts. Students explore the challenges and opportunities of building ventures across different markets, regulatory environments, and cultural settings. Topics include international market entry strategies, cross-cultural team management, global supply chain considerations, and adapting business models for diverse markets. The course covers emerging market opportunities, global startup ecosystems, and the impact of geopolitical factors on international ventures. Students develop global venture strategies through case analyses and projects, gaining skills in navigating the complexities of building and scaling businesses in the global marketplace.',
3.0, 40),

('MIST', '330', 'Human-Computer Interaction',
N'This course examines the design and evaluation of user interfaces and interactive systems. Students explore usability principles, user-centered design processes, accessibility standards, and interaction design patterns. Topics include user research methods, wireframing, prototyping tools, usability testing, and cognitive aspects of human-computer interaction. The course covers designing for diverse users across web, mobile, and emerging platforms including voice interfaces and augmented reality. Students complete design projects involving the full UCD process from user research through prototype evaluation, developing practical skills in creating intuitive, accessible, and effective digital experiences.',
3.0, 35),

('MIST', '340', 'Big Data Technologies',
N'An introduction to big data concepts, architectures, and processing frameworks for handling large-scale datasets. Students explore the Hadoop ecosystem, Apache Spark, distributed storage systems, and stream processing technologies. Topics include data ingestion pipelines, batch and real-time processing, data lake architectures, and NoSQL databases. The course covers practical applications of big data technologies in business intelligence, analytics, and machine learning workflows. Through hands-on lab exercises, students gain experience working with distributed computing environments, developing skills in processing and analyzing massive datasets to extract meaningful business insights.',
3.0, 30),

('CS', '450', 'Computer Vision and Image Processing',
N'An advanced course covering fundamental and applied concepts in computer vision and digital image processing. Students explore image acquisition, filtering, edge detection, feature extraction, and object recognition techniques. Topics include convolutional neural networks for visual recognition, image segmentation, object detection frameworks, and video analysis. The course covers applications in autonomous systems, medical imaging, surveillance, and augmented reality. Through programming projects using Python and deep learning frameworks, students implement computer vision pipelines and develop practical skills in building systems that can interpret and analyze visual information from the real world.',
3.0, 30);
