#!/usr/bin/env python

import asyncio

from metagpt.actions import Action
from metagpt.environment import Environment
from metagpt.roles import Role
from metagpt.team import Team

# Define Actions
web_scraping = Action(name="Web Scraping", instruction="Scrape data from websites.")
verifier = Action(name="Verifier", instruction="Verify the scraped data for accuracy.")
page_navigation = Action(name="Page Navigation", instruction="Navigate through web pages to find specific information.")
auto_email_sender = Action(name="Auto Email Sender", instruction="Send automated emails based on collected data.")

# Define Roles
web_scraping_agent = Role(name="Web Scraping Agent", profile="Collect data from websites", actions=[web_scraping])
verifier_agent = Role(name="Verifier Agent", profile="Verify data accuracy", actions=[verifier])
page_navigating_agent = Role(name="Page Navigating Agent", profile="Navigate web pages for information", actions=[page_navigation])
auto_email_sender_agent = Role(name="Auto Email Sender Agent", profile="Send automated emails", actions=[auto_email_sender])

# Create an environment
env = Environment(desc="Data Deletion Agent Simulation")

# Create a team with the defined roles
team = Team(investment=10.0, env=env, roles=[web_scraping_agent, verifier_agent, page_navigating_agent, auto_email_sender_agent])

async def main():
    # Run the team with a topic idea
    topic = "Data deletion analysis"
    await team.run(idea=f"Topic: {topic}. Under 100 words per message.", send_to="Web Scraping Agent", n_round=3)
    print("Simulation completed.")

if __name__ == "__main__":
    asyncio.run(main())
