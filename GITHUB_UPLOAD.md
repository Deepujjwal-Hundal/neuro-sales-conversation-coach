# Upload to GitHub - Instructions

## Step 1: Create GitHub Repositories

1. Go to https://github.com/new
2. Create a new repository named: `neuro-sales-conversation-coach`
   - Description: "AI-powered sales conversation analysis tool with video/audio support"
   - Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

## Step 2: Push to GitHub

Run these commands in your terminal:

```bash
cd "D:\Python codes\neuro-sales-conversation-coach"

# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/neuro-sales-conversation-coach.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Alternative: Using SSH (if you have SSH keys set up)

```bash
git remote add origin git@github.com:YOUR_USERNAME/neuro-sales-conversation-coach.git
git branch -M main
git push -u origin main
```

## If you need to authenticate:

- GitHub no longer accepts passwords for HTTPS
- Use a Personal Access Token (PAT) instead:
  1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. Generate new token with `repo` scope
  3. Use the token as your password when prompted

## Verify Upload

After pushing, visit:
`https://github.com/YOUR_USERNAME/neuro-sales-conversation-coach`

You should see all your files there!

