
**URL:** https://www.flagsmith.com/blog/infrastructure-costs

---

Product
Solutions
Resources
Pricing
Sign In
Contact Us
All articles
TABLE OF CONTENTS
The Evolution (and costs) of our SaaS Infrastructure 
Infra Round 1: 2 hours of effort
Oh, actually now we have actual customers LOL
Round 1 Wrap Up
Infra Round 2: 2 days of effort
Elastic Beanstalk is actually great, but a bit terrifying
Round 2 Wrap Up
Infra Round 3: Containerisation Firecrackers
What do we think of ECS?
Round 3 Wrap Up
Infra Round 4: What’s next
The actual infrastructure costs of running SaaS at scale (billions of requests/month)
Ben Rometsch

This is a two-part series. Find the second article here.

In this article we are going to share three main things: 

The evolution of our infrastructure over the last few years
The actual costs of our SaaS offering at Flagsmith
Our opinion on the role of feature flag services

Before we dive in, one important call-out: We provide our feature management product to customers in three ways depending on how they want to have it managed: Fully Managed SaaS API, Fully Managed Private Cloud SaaS API and Self-Hosted. The infrastructure costs that we are sharing is for our customers that leverage our Fully Managed SaaS API offering (try it free: https://www.flagsmith.com/) which represents a portion of the total flags being delivered among those three product offerings. 

The Evolution (and costs) of our SaaS Infrastructure 

Late last year, the Flagsmith SaaS API crossed the threshold of a billion flags served in one month.

To help others learn from our mistakes and successes, we’re sharing how our infrastructure changed over this period, the money we spent, the choices we made, and why we made them.

Infra Round 1: 2 hours of effort

Flagsmith started as a side project of Solid State Group - the agency I started 21(!) years ago. We had been building side projects for a while and had perfected the art of building as much as possible as quickly as possible. That meant leaning on frameworks like Django and Django Rest Framework to do as much heavy lifting as possible. But it also meant that our infrastructure was optimised for 2 things: 1) cost and 2) minimal effort to stand up. 

When you have zero customers, lean into that. 

We already had a Hetzner server kicking around that wasn’t doing much, so we installed dokku;  a great project that gives you a self-hosted Heroku-like deployment platform but with minimal costs. We set up a super simple CICD via GitLab CI that would push changes to our `main` branch to dokku as we went. Postgres was up and running in 2 minutes. Sorting the DNS and LetsEncrypt SSL certificate was pretty easy. And that was it. Total time spent was maybe 2 hours. 

We had no redundancy, very limited backups, no elastic scaling and a single box that was a big single point of failure. Like I said, we also had zero customers, so who cares? 

Oh, actually now we have actual customers LOL

Pretty soon after releasing the platform and trying to drum up some traffic, we noticed a huge increase in traffic to our API. Back then we were hacking Google Analytics to track our API volume - it was free which was basically 90% of the decision making process. After some further investigation we realised a fairly large UK lottery operator was using the platform on some highly trafficked pages. This was great: people are using our platform! but also terrifying: people are using our platform!

We were super busy building out basic features at that point in time; we really didn't want to invest any further effort into our infrastructure. People don’t buy your infrastructure, they buy your product. But we had the problem; what we refer to as “the B2B2C problem”. 

It goes something like this. If we sign up a customer, and they put our JS SDK on their website, we aren’t serving that 1 customer; we are serving all of their customers. So 1 new person using our platform could mean suddenly serving 100 million additional flags a month. If you are direct B2C, your scaling looks way less crazy, as additional users come in one at a time. But if you are B2B2C, you might suddenly have to triple your requests served literally from one second to the next. 

And this is actually harder when you are small! When you are large, one large customer might mean an additional 10% load on your API, but when you are small, one large customer might mean 10x your load! It’s the power of small numbers. Or something. 

Anyway, once we saw this happening in real life we decided it was time to put our professional trousers on. Hetzner and dokku had been great, but it was making us super nervous. 

Round 1 Wrap Up
Total cost: ~$40 per month
Peak Flags served per month: 20 million
Anxiety Levels: 5/10 anxious but this all still feels like a side project
Infra Round 2: 2 days of effort

We know how to do this; we do it for our clients all the time! But in this case no-one was paying for it, so we wanted it to be clinically quick. We already had a Heroku-like deployment process. Elastic Beanstalk was pretty close to that, but with things like auto-scaling and managed databases; professional trousers stuff. 

So we went with AWS Beanstalk, EU London region (it was in the EU at the time #facepalm). It’s sort of in the middle of the world, and we care about latency a little. RDS Postgres works. It does automated backups and security updates.

Beanstalk has loads of horrible sharp edges it turns out, but we plowed on and had things up and running in a couple of days. We stood up an Aurora Postgres database, and copied the data across. We had around 30 seconds of downtime where we finished migrating any new data, then pointed our Dokku instance over to AWS and updated our DNS records. Yes, we could have spent another month engineering a zero downtime migration, but these are the hard choices you have to make.

Elastic Beanstalk is actually great, but a bit terrifying

We were actually surprised how far this setup got us. We only recently migrated off it, props to Beanstalk - it might be the most unloved AWS product there is, but it works and it’s stable. 

It does have a propensity, when you are doing something unusual like you know, deploying your software, where it sort of gives up and then sits in a weird state for half an hour whilst you are crying, but it almost always righted itself and redeployments then worked. We never really got to the bottom of why this happened, but in almost all cases it didn’t drop any requests, which was rapidly becoming our most important consideration.

Beanstalk also makes it super easy to scale out your application server layer. This worked perfectly, and was the main reason why we stayed on it for so long. At this point, the bottleneck of the platform started moving from the application server to the database and the number of connections it was having to service. At peak we got up to around 70 small app server instances. By this point our concurrent database connections were becoming our bottleneck.

Round 2 Wrap Up
Total Cost: Elastic costing eh! Anything from $300 to $800 per month - Cloudfront is expensive and there’s nothing you can do about it
Peak Flags Served per month: 600 million
Anxiety Levels: Still high as hell during deployments but getting a text in the middle of the night is less stressful
Infra Round 3: Containerisation Firecrackers

Over time, Docker and the containerisation of everything meant that our production SaaS infrastructure was looking less and less like that of our Enterprise customers as time went by. We also realised that Beanstalk was basically on autopilot, and there were some python dependencies we really needed that weren’t available on the platform. 

So we made the decision to move to AWS ECS and Fargate. We were already building Docker images for our open source and Enterprise users, so it shouldn't be too tricky, right? By this time our application had grown to dozens of environment variables and the Beanstalk deployment had grown some hairballs here and there to kludge some stuff like SSL rewrites. 

Luckily we didn’t have to move the data, which is almost always the hard part. So we stood up a new ECS cluster and used the excellent support AWS load balancers provide for splitting traffic between our two different sets of infrastructure. Over the course of a couple of weeks we migrated 100% of the traffic over to ECS and the Beanstalk infra dropped away like a well used rocket first stage. 

What do we think of ECS?

ECS is superb and we love it a lot. 

Round 3 Wrap Up
Total Cost: Actually dropping on a $-per-request basis. We upgraded to python 3.10 and more modern gunicorn, and the Docker images are more performant than the Beanstalk infra. We are now spending around $1,200 per month which splits roughly evenly between RDS, ECS and Cloudfront/bandwidth.
Peak Flags Served per month: Well into the billions
Anxiety Levels: Actually pretty low. ECS is rock solid and has blue/green deployments built in. We’ve yet to get it into the fugue state that we often managed to with Beanstalk.
Infra Round 4: What’s next

It’s coming up! We’re about to migrate our SDK traffic to a globally distributed and replicated Edge API. We’ve been working on it way too long but we’re going to deploy it very soon, and will be writing that up next! 

If you are curious about our performance, please check out our status page. If you want to support us, please give us a star on Github! If you need feature flags and want to partner with a team that is in it for the reasons I outlined above; feel free to sign up for a free account and give it a try! 

Lets go!

This is a two-part series. Read the second article about the infrastructure costs of running a global Edge API here.

About the author

Flagsmith co-founder. Besides Flagsmith, Ben has founded several other companies, and he currently serves on the Governance Board of OpenFeature, a CNCF Sandbox Project. He's an advocate for open standards and open source and also hosts “The Craft of Open Source" podcast, where he interviews creators and maintainers from the open-source community.

Related Articles
October 24, 2025
Progressive Delivery for Building LLM-Powered Features
Pete Hodgson
October 23, 2025
What is the Four Eyes Principle? A Developer's Guide to Safer Flag Changes
Tanaaz Khan
October 17, 2025
De-Risking AI Adoption: How Feature Flags Help Enterprises Move Fast Without Breaking Trust
Adrian Gregory
October 7, 2025
Monitoring Feature Flag Performance with Flagsmith, Prometheus, and Grafana
Daniel Efe
September 25, 2025
What is Release Management and How Does it Work in Regulated Industries?
Tanaaz Khan
September 17, 2025
Banking and Modern Observability: Dynatrace Insights
Andreas (Andi) Grabner
September 4, 2025
No More Hardening Phases: Testing in the Age of Continuous Deployment
Pete Hodgson
September 1, 2025
How Modernisation is Changing Open Source Banking
Rob Moffat
August 5, 2025
Use Grafana to Track Feature Health in Flagsmith
Mia Loiselle
August 28, 2025
6 Lessons From the World's Best Open-Source Founders
Ben Rometsch
August 27, 2025
Feature Toggles and Feature Flags: Understanding the Key Differences
Tanaaz Khan
August 25, 2025
8 Types of Deployment Strategies (And How Feature Flags Help)
Ben Rometsch
July 31, 2025
Moving to Progressive Delivery with Feature Flags
Ben Rometsch
July 11, 2025
Top 7 Feature Flag Tools for Enterprises in 2025
Tanaaz Khan
June 3, 2025
Moving Fast, Without Breaking Things: Modern Software Delivery with Feature Flags
Pete Hodgson
June 4, 2025
TypeScript Feature Flags: A Next.js Example
Michael Dinerstein
May 14, 2025
Embracing Modernisation in Banking Through Platform Engineering
Benjamin Brial
May 9, 2025
Transitioning to Modern Authorisation Management
Alex Olivier
April 22, 2025
What Are Feature Flags? Everything Engineering Teams Need to Know
Ben Rometsch
April 7, 2025
A Conversation with Komerční Banka's Chief Software Architect
Mia Loiselle
March 26, 2025
GitOps for Feature Flags Using Terraform and Terrateam
Malcolm Matalka
March 25, 2025
Why It’s Time to Test in Production (+ How to Do It Safely)
Tanaaz Khan
January 22, 2025
How We Improved Our Docker Image Security Using Chainguard's Wolfi
Kim Gustyr
January 7, 2025
6 Best Enterprise-Grade Harness Alternatives & Competitors
Tanaaz Khan
October 28, 2024
How to Roll out Pricing Changes With Zero Customer Complaints
Matthew Elwell
September 16, 2024
How to Use Feature Flags for Trunk-Based Development
Kyle Johnson
August 21, 2024