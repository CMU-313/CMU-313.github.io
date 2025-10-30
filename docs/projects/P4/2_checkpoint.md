# Final (Implementation and Evaluation)

## Final LLM Experiment Implementation (30 points)

The final step is to implement this LLM feature into your team's NodeBB project. Your implementation should include the UI code you integrated in Checkpoint #2. You should also integrate the code you developed as a part of the LLM experiment, but you may modify it as needed to successfully integrate the functionality into your code.
**Because this is the last Project to use NodeBB, commit to your repo, and we will grade your final repository state**!

Reach out to your TA if you have any questions. 

## Evaluation Report (30 points)

Now that you’ve experimented with an LLM integration, write a report that summarizes your findings for the rest of the team. In particular, you will need to decide whether your findings justify completing and shipping this feature.

TODO: LLM interaction space
Get rid of assessing LLM suitability
Having a definition of done, when is it good enough
Add for each person what model you tested, what prompts you used, what accuracy you got

Your report should include the following with clear headings:

**1. Introduction (&lt;0.5 pages)**

Provide a brief introduction to the LLM integration you’re evaluating, and the context of its use, i.e. the translation feature.

**2. LLM integration (&lt;1 page)**

Describe the end-to-end implementation of your final solution to translating posts. Given an arbitrary post in any language, how do you integrate with an LLM to return an answer? Feel free to include any prompts and diagrams.

**4. Evaluation Results (&lt;0.5  page)**

Provide a summary of the results from applying the evaluation strategy on your final LLM experiment. Feel free to include any evidence/output from your notebook.

**5. Operational Costs (&lt;0.5 pages)**

Based on the pricing of your chosen LLM, how much will it cost to provide users with this feature? How long does it take to translate a post? State any assumptions made in making these estimates. Is the cost associated with providing this feature reasonable?

**6. Final Recommendation (&lt;0.5 pages)**

Provide a final decision on whether the translation feature should be implemented based on the evaluation results, operational costs and other relevant factors.

On Gradescope submit the following:

* Link to your Colab notebook (with output) that contains your code, analysis. Make sure it is editable so that we can run the notebook if necessary.
* PDF of your evaluation report

## Grading
To receive full credit for the first checkpoint, we expect:

- [ ] An uploaded PDF design document outlining your research into the existing codebase architecture, the quality requirements considered by your team, alternative solutions, and a final justification & timeline for your selected integration plan
- [ ] A link to your Colab notebook completing all of the setup and basic LLM experiment steps outlined by the previous section

To receive full credit for the second checkpoint, we expect:

- [ ] A functional integration of the UI code into your NodeBB application.
- [ ] A preliminary implementation of the translation feature using the starter code, including CI with unit and mock tests.
- [ ] Integrating NodeBB and the translation service.

To receive full credit for the final deadline, we expect:

- [ ] A functional translation feature, as described in your design document, integrated into your NodeBB application.
- [ ] An uploaded PDF report discussing your evaluation findings addressing all the sections outlined above

