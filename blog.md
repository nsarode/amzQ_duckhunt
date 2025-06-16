# Building a Duck Hunt Game with Amazon Q: A Bioinformatician's Journey into Game Development

As a bioinformatician and data scientist, my days typically revolve around genomic data analysis and building machine learning models for biological applications. Game development? That's a world I've never ventured into—until now. Thanks to Amazon Q, I was able to create a fully functional Duck Hunt game without writing a single line of code myself. Here's my experience participating in Amazon's Build Games with Agentic Coding in CLI Challenge.

## The Challenge

When I first heard about Amazon's Build Games Challenge, I was intrigued but skeptical. Could I, someone with zero game development experience, actually create a playable game? The challenge invited participants to use Amazon Q Developer CLI to build classic games, and I decided to test its capabilities by recreating Duck Hunt, the iconic Nintendo shooting game from the 1980s.

## Getting Started with Amazon Q

The process began with a simple conversation with Amazon Q through its CLI interface. I described what I wanted to build—a first-person duck hunting game with score tracking, time limits, and increasing difficulty. To my surprise, Amazon Q immediately understood the concept and started generating code for a 3D game using the Ursina engine, a Python game development framework I'd never heard of before.

## From Concept to Playable Game

Within minutes, Amazon Q had generated a complete Python script that included:
- A 3D environment with sky and ground
- Duck entities that move randomly through the game world
- A first-person camera with mouse aiming
- Shooting mechanics with hit detection
- Score tracking and high score system
- Game states (menu, playing, paused, game over)
- UI elements for all game screens

The most surprising part? When I ran the code, it actually worked! I was immediately able to aim, shoot, and hit ducks flying across the screen. The score system tracked my hits and misses, and the game properly cycled through different states.

## Refining the Experience

Of course, the initial version wasn't perfect. I encountered a few issues that needed fixing:
1. **Mouse lag**: The mouse response was sluggish, making aiming difficult
2. **Window sizing**: The game launched in fullscreen with no easy way to resize
3. **Scoring bugs**: Hitting ducks didn't always increase my score

This is where Amazon Q truly impressed me. I simply described these issues conversationally, and it diagnosed and fixed each problem. For the mouse lag, it optimized the camera controller code. For window sizing, it added keyboard shortcuts (F9/F10 to resize, F11 for fullscreen). For the scoring bug, it fixed variable scope issues in the code.

## GitHub Integration and Documentation

Amazon Q didn't just help with the game code. It also:
- Created a GitHub repository for the project
- Generated a comprehensive README with installation instructions
- Added Docker configuration for cross-platform compatibility
- Created appropriate badges and licensing for the repository
- Documented future improvement possibilities

## Strengths of Amazon Q for Non-Developers

As someone who doesn't develop games, these strengths stood out to me:

1. **Domain Knowledge**: Amazon Q understood game development concepts and patterns without me needing to explain them.

2. **Framework Selection**: It chose appropriate tools (Ursina engine) that balanced ease of use with the capabilities I needed.

3. **Complete Solutions**: Rather than just code snippets, it provided end-to-end solutions including game logic, UI, and state management.

4. **Debugging Capabilities**: When issues arose, Amazon Q could diagnose and fix them based on error messages or my descriptions.

5. **Project Management**: It handled the entire software lifecycle from code creation to documentation and deployment configuration.

## Weaknesses and Limitations

Despite its impressive capabilities, I did notice some limitations:

1. **Performance Optimization**: The initial code wasn't optimized for performance, requiring several iterations to fix mouse lag issues.

2. **Asset Management**: The game lacked proper asset handling, showing warnings about missing models and sounds.

3. **Error Handling**: Some syntax errors made it into the code that had to be fixed later.

4. **Testing Gaps**: There was no automated testing included, which would be important for a larger project.

5. **Architecture Decisions**: The code was monolithic rather than modular, which could limit extensibility.

## Recommendations for Improvement

Based on my experience, here are some recommendations for improving Amazon Q:

1. **Performance Templates**: Offer optimized templates for different types of applications, including games with responsive controls.

2. **Asset Pipeline Integration**: Provide better guidance on asset management and perhaps even generate placeholder assets.

3. **Architecture Patterns**: Suggest modular code organization from the start rather than requiring refactoring later.

4. **Testing Generation**: Automatically include basic tests for critical functionality.

5. **Interactive Debugging**: Improve the ability to interactively debug issues rather than requiring multiple back-and-forth exchanges.

## Conclusion

As a bioinformatician with no game development experience, I was able to create a functional Duck Hunt game without writing any code myself. Amazon Q handled everything from game mechanics to GitHub setup. While there's room for improvement, the experience demonstrated how AI coding assistants are democratizing software development across domains.

The most valuable insight for me was seeing how my data science skills—clear problem definition, systematic debugging, and iterative improvement—transferred perfectly to this new domain when paired with Amazon Q's technical capabilities. This tool doesn't just write code; it bridges knowledge gaps and enables domain experts to create software outside their specialization.

Would I use Amazon Q again for projects outside my expertise? Absolutely. It's not just a coding assistant—it's a knowledge translator that helps specialists like me venture confidently into new technical territories.

---

*This Duck Hunt game was created as part of [Amazon's Build Games with Agentic Coding in CLI Challenge](https://community.aws/content/2y6egGcPAGQs8EwtQUM9KAONojz/build-games-challenge-build-classics-with-amazon-q-developer-cli), showcasing the capabilities of Amazon Q Developer CLI for game development.*
