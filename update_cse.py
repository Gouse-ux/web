
import re

def restructure_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Paper Presentation
    paper_search = r'(<div class="event-details">\s*<h4>Paper Presentation</h4>.*?<div class="event-footer">.*?</div>\s*</div>)'
    paper_replacement = """<div class="event-details">
                        <h4>Paper Presentation</h4>
                        <div class="event-meta">
                            <span><i class="fas fa-clock"></i> 11:00 AM - 3:00 PM</span>
                            <span><i class="fas fa-users"></i> 1/2</span>
                            <span><i class="fas fa-trophy"></i> Winner: 2000/- Runner-up: 1000/-</span>
                        </div>
                        <p class="event-description">Showcase your research and presentation skills in the Paper
                            Presentation event! Participants will present their well-structured papers, demonstrating
                            originality, analytical thinking, and effective communication. The event provides a platform
                            to share innovative ideas and gain valuable insights.</p>
                        
                        <div class="event-info-list">
                            <div class="info-item">
                                <i class="fas fa-thumbtack"></i>
                                <span><strong>Registration Fee:</strong> ₹200/-</span>
                            </div>
                            <div class="info-item">
                                <i class="fas fa-gift"></i>
                                <span><strong>Prizes:</strong> Exciting Prizes for Winners!</span>
                            </div>
                            <div class="info-item">
                                <i class="fas fa-rocket"></i>
                                <span>Register now and make your mark!</span>
                            </div>
                        </div>

                        <div class="event-footer">
                            <a href="https://rzp.io/rzp/paper-cse" target="_blank" class="btn">Register Now</a>
                        </div>
                    </div>"""

    # 2. Hackathon
    hackathon_search = r'(<div class="event-details">\s*<h4>Hackathon \[5hrs\]</h4>.*?<div class="event-footer">.*?</div>\s*</div>)'
    hackathon_replacement = """<div class="event-details">
                        <h4>Hackathon [5hrs]</h4>
                        <div class="event-meta">
                            <span><i class="fas fa-clock"></i> 10:00 AM - 03:00 PM</span>
                            <span><i class="fas fa-users"></i> 1-3</span>
                            <span><i class="fas fa-trophy"></i> Winner: 3000/- Runner-up: 2000/- Runner-up2: 1000/-</span>
                        </div>
                        <p class="event-description">Gear up for an intense 5-hour Hackathon where innovation meets
                            execution! This event challenges participants to brainstorm, develop, and present creative
                            solutions within a limited timeframe, testing their problem-solving and technical skills.</p>
                        
                        <div class="event-info-list">
                            <div class="info-item">
                                <i class="fas fa-thumbtack"></i>
                                <span><strong>Registration Fee:</strong> ₹300/-</span>
                            </div>
                            <div class="info-item">
                                <i class="fas fa-gift"></i>
                                <span><strong>Prizes:</strong> Exciting Prizes for Winners!</span>
                            </div>
                            <div class="info-item">
                                <i class="fas fa-laptop-code"></i>
                                <span>Register now and code your way to victory!</span>
                            </div>
                        </div>

                        <div class="event-footer">
                            <a href="https://rzp.io/rzp/WzrOXgY" target="_blank" class="btn">Register Now</a>
                        </div>
                    </div>"""

    # 3. Code Buzz
    codebuzz_search = r'(<div class="event-details">\s*<h4>Code Buzz</h4>.*?<div class="event-footer">.*?</div>\s*</div>)'
    codebuzz_replacement = """<div class="event-details">
                        <h4>Code Buzz</h4>
                        <div class="event-meta">
                            <span><i class="fas fa-clock"></i> 02:00 PM - 04:00 PM</span>
                            <span><i class="fas fa-users"></i> 1/2</span>
                            <span><i class="fas fa-trophy"></i> Winner: 2000/- Runner-up: 1000/-</span>
                        </div>
                        <p class="event-description">Put your coding skills to the test in Code Buzz! This event
                            challenges participants to think logically, solve problems efficiently, and showcase their
                            programming expertise. Compete against the best and prove your coding prowess!</p>
                        
                        <div class="event-info-list">
                            <div class="info-item">
                                <i class="fas fa-thumbtack"></i>
                                <span><strong>Registration Fee:</strong> ₹200/-</span>
                            </div>
                            <div class="info-item">
                                <i class="fas fa-gift"></i>
                                <span><strong>Prizes:</strong> Exciting Prizes for Winners!</span>
                            </div>
                            <div class="info-item">
                                <i class="fas fa-bolt"></i>
                                <span>Register now and let the code speak!</span>
                            </div>
                        </div>

                        <div class="event-footer">
                            <a href="https://rzp.io/rzp/U90hf3T8" target="_blank" class="btn">Register Now</a>
                        </div>
                    </div>"""

    content = re.sub(paper_search, paper_replacement, content, flags=re.DOTALL)
    content = re.sub(hackathon_search, hackathon_replacement, content, flags=re.DOTALL)
    content = re.sub(codebuzz_search, codebuzz_replacement, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    restructure_html('cse.html')
