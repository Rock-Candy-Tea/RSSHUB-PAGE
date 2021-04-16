
---
title: 'Git 分支管理策略与工作流程'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=5860'
author: Dockone
comments: false
date: 2021-04-16 08:08:46
thumbnail: 'https://picsum.photos/400/300?random=5860'
---

<div>   
<br>【编者的话】Git 是目前世界上最先进的分布式版本控制系统。它使我们更方便的跟踪，管理和组织代码。也帮助了我们更好的与其他开发者进行协作开发。但是没有规矩不成方圆。协作开发必须有一个规范来约束各个贡献者的行为。这个规范就是 Git 工作流程（Git Workflow），也为我们规范各个分支管理策略等行为。<br>
<br>Git 工作流程是有关如何使用 Git 以高效协作开发的规则或策略建议，下文这些常见工作流程只是作为指导参考，这些工作流不是一成不变的，我们应该根据自己的项目选择或制定合适自己的工作流。<br>
<h3>集中式工作流</h3>首先我们来介绍最简单粗暴的集中式工作流，如果你用过 <a href="https://subversion.apache.org/">SVN</a>，那么你可以无痛切换到 Git 集中式工作流。该工作流只用到 <code class="prettyprint">master</code> 这一个主分支来维护我们的代码，这也是该工作流的主要工作方式。<br>
<h4>工作流程示例</h4>1、首先 clone 远程仓库到本地<br>
<pre class="prettyprint">git clone ssh://user@host/path/to/repo.git<br>
</pre><br>
2、然后在本地的 master 分支做出修改完成开发后，创建一个提交<br>
<pre class="prettyprint">git status # 查看本地仓库的修改状态<br>
git add # 暂存文件<br>
git commit # 提交文件<br>
</pre><br>
3、然后推送到远程仓库<br>
<pre class="prettyprint">git push origin master<br>
</pre><br>
4、如果此时本地仓库与远程仓库有了分歧，Git 将拒绝操作并报错。这时我们就应该先 pull 远程仓库的修改到本地仓库后再解决重新推送<br>
<pre class="prettyprint">git pull --rebase origin master<br>
</pre><br>
5、如果有冲突，Git 会在合并有冲突的提交处暂停 rebase 过程，并报出错误信息，我们在解决掉冲突后可以使用一下命令将更改加入暂存区后继续只能执行 rebase：<br>
<pre class="prettyprint">git add <some-file> <br>
git rebase --continue<br>
</pre><br>
如果遇到一个搞不定的冲突，这可以使用一下命令来终止 rebase<br>
<pre class="prettyprint">git rebase --abort<br>
</pre><br>
<h4>主要遵循原则</h4><ul><li>只用到 <code class="prettyprint">master</code> 这一个分支，所有的修改都推送到 master 分支</li><li><code class="prettyprint">master</code> 分支代表了项目的正式发布版本，所以提交历史应该被尊重且是稳定不变的</li><li>pull 代码时, 最好使用 rebase 而不是生成一个 merge commit</li></ul><br>
<br><h4>优点</h4><ul><li>集中式工作流主要优点是简单，非常适合小型团队</li><li>对于要从 <code class="prettyprint">SVN</code> 迁移过来的团队来说很友好</li></ul><br>
<br><h4>缺点</h4><ul><li>当您的团队规模扩大时，上面详述的冲突解决过程可能会成为瓶颈</li><li>完全没有发挥 Git 的优势，在实际使用 Git 协作的项目开发中很少使用集中式工作流</li></ul><br>
<br>如果在稍大的团队中使用前面的集中式工作流，那么可能会在解决冲突中浪费很多时间。在实际开发中我们基本上都是都  <a href="https://en.wikipedia.org/wiki/Feature-driven_development">功能驱动式开发</a>，基于功能需求，创建相应的分支进行开发，完成开发合并到主分支后再被删除掉。接下来我们介绍的三个工作流：GitHub Flow，Git Flow 及 GitLab Flow 都是基于不同的分支管理策略运作的。<br>
<h3>GitHub Flow 工作流</h3>GitHub Flow 是一个轻量级的基于分支的工作流程。它由 <a href="https://guides.github.com/introduction/flow/">GitHub</a>  在 2011 年创建。分支是 Git 中的核心概念，并且 GitHub 工作流程中的一切都以此为基础。<br>
<br>最重要的的一点就是：<strong><code class="prettyprint">main</code> / <code class="prettyprint">master</code> 分支中的任何内容始终都是可部署的</strong>。其他分支（功能分支）创建用于新功能和错误修复的工作，并且在工作完成并经过检查后，这些分支将合并回到主分支中后删除。这些分支名应该是具有描述性的如 <code class="prettyprint">refactor-authentication</code>,  <code class="prettyprint">user-content-cache-key</code>，<code class="prettyprint">make-retina-avatars</code>。<br>
<h4>工作流程示例</h4>1、首先 clone 远程仓库到本地<br>
<pre class="prettyprint">git clone ssh://user@host/path/to/repo.git<br>
</pre><br>
2、根据要实现的功能创建一个新的分支，分支名应该具有描述性，如实现鉴权功能：feature-auth<br>
<pre class="prettyprint">git checkout -b feature-auth<br>
</pre><br>
3、然后将新工作提交到该分支下，并定期将工作推送到远程仓库<br>
<pre class="prettyprint"># 创建一个 commit<br>
git status # 查看本地仓库的修改状态<br>
git add # 暂存文件<br>
git commit # 提交文件<br>
<br>
# 将分支推送到远程仓库<br>
git push --set-upstream origin feature-auth<br>
</pre><br>
4、当你需要帮助或者反馈，或是你觉得你已经完成该功能的工作准备合进主分支的时候创建 <a href="https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests">pull request</a><br>
<br>5、当你的这部分工作在 pull request 中，被 review 以及 approved 后，则可以合并到主分支。<br>
<pre class="prettyprint">git checkout master<br>
git pull<br>
git pull origin feature-auth<br>
git push<br>
</pre><br>
6、合并到主分支后，应立即对其进行部署<br>
<h4>主要遵循原则</h4><ol><li><code class="prettyprint">master</code> 分支中的任何内容都是可部署的</li><li>要进行新的工作，需要从主分支 <code class="prettyprint">master</code> 创建出一个分支，并给出描述性的名称（如：<code class="prettyprint">new-oauth2-scopes</code>）</li><li>本地的修改提交到该分支，并定期将你的工作推送到服务器上的同一命名分支</li><li>当你需要反馈或帮助时，或者你认为分支已准备好进行合并时，请打开一个 <a href="https://help.github.com/send-pull-requests/">Pull Request</a></li><li>在其他人 Review 并 Approved 该功能后，你可以将其合并到 <code class="prettyprint">master</code></li><li>合并并推送到后主分支 <code class="prettyprint">master</code>，你可以并且应该立即进行部署</li></ol><br>
<br><h4>优点</h4><ul><li>相比于前文介绍的集中式流程更为合理实用，可以减少工作中的冲突</li><li>由于工作流程的简单性，此 Git 分支策略对进行持续交付和持续集成很友好。</li><li>当需要在生产中维护单个版本时，它是理想的选择</li><li>这个 Git 分支策略非常适合小型团队和 Web 应用程序</li></ul><br>
<br><h4>缺点</h4><ul><li>这种 Git 分支策略无法同时支持多个版本的代码的部署</li><li>没有解决部署、环境区分、 releases、Bug 修复相关的问题</li><li>生产代码容易变得不稳定</li></ul><br>
<br><h3>Git Flow 工作流</h3>基于功能分支的工作流是一中相当灵活的方式。但是问题也是有时候过于灵活。对于大型团队，常常需要给不同分支分配一个更具体的角色。 Git Flow 工作流是管理功能开发、预发布和维护的常用模式。<br>
<br>Git Flow 是最早诞生并且相当流行的工作流程。它由 <a href="http://nvie.com/posts/a-successful-git-branching-model/">Vincent Driessen</a> 于 2010 年创建。Git Flow 工作流定义了一个围绕项目发布的严格分支模型。虽然比 GitHub Flow 的功能分支工作流复杂一点，但提供了用于一个健壮的用于管理大型项目的框架。<br>
<br>Git Flow 工作流没有用超出功能分支工作流的概念和命令，Git Flow 为不同的分支分配一个很明确的角色，并定义分支之间如何和什么时候进行交互。<br>
<h4>工作流程示例</h4>假设你已经创建好了中央仓库，并且已将其 clone 到本地。<br>
<br>1、首先我们来从主分支创建一个开发分支 develop， 并推送到服务器<br>
<pre class="prettyprint">git branch develop<br>
git push -u origin develop<br>
</pre><br>
以后这个分支将会包含了项目的全部历史，而  <code class="prettyprint">master</code>  分支将只包含了部分历史<br>
<br>2、接下来我们开始开发新功能，基于 develop 分支创建新的功能分支<br>
<pre class="prettyprint">git checkout -b some-feature develop<br>
</pre><br>
并在自己的功能分支上进行开发、创建提交：<br>
<pre class="prettyprint">git status # 查看本地仓库的修改状态<br>
git add # 暂存文件<br>
git commit # 提交文件<br>
</pre><br>
3、当你在你的分支上完成工作，准备好进行合并时，请打开一个 Pull Request，用于合并到 <code class="prettyprint">develop</code> 分支。如果你的团队没使用 Pull Request 则可以直接合并到本地的 develop 分支然后推送到中央仓库。<br>
<pre class="prettyprint">git pull origin develop<br>
git checkout develop<br>
<br>
git merge --no-ff some-feature<br>
git push<br>
# 删除本地分支<br>
git branch -d some-feature<br>
</pre><br>
并且在功能分支合并后应该立即删除<br>
<br>4、当我们的 <code class="prettyprint">develop</code> 分支进行到需要发布时，需要从 <code class="prettyprint">develop</code> 分支创建一个新的发布分支，命名为 <code class="prettyprint">release-*</code> 或 <code class="prettyprint">release/*</code>。这一步也确定了发布的版本号：<br>
<pre class="prettyprint">git checkout -b release-0.1.0 develop<br>
</pre><br>
这个分支是一个预发布的版本，只做 bug 修复、文档生成等面向发布的任务。新功能不再添加到这个分支上<br>
<br>5、经过一系列测试确认没有问题，准备好了对外发布后，我们需要将发布分支合并到 master 分支，并打下 tag<br>
<pre class="prettyprint">git checkout master<br>
git merge --no-ff release-0.1<br>
git push<br>
</pre><br>
<pre class="prettyprint">git tag -a 0.1 -m "release 0.1 publish" master<br>
git push --tags<br>
</pre><br>
6、同时我们还需要将这个发布分支合并回去 master 分支<br>
<pre class="prettyprint">git checkout develop<br>
git merge --no-ff release-0.1.0<br>
git push <br>
</pre><br>
最后我们还需要删除掉这个发布分支 release-0.1.0<br>
<br>7、如果我们的线上版本出现问题时，就需要创建一个维护分支，用于快速给产品打补丁。这个维护分支需要从 <code class="prettyprint">master</code> 分支上创建，提交修改以解决问题，然后再直接合并回 <code class="prettyprint">master</code> 分支：<br>
<pre class="prettyprint">git checkout -b hotfix-auth master<br>
</pre><br>
修复完成后将其合并到 master 分支<br>
<pre class="prettyprint">git checkout master<br>
git merge --no-ff hotfix-auth<br>
git push<br>
</pre><br>
同时打下新的 tag<br>
<pre class="prettyprint">git tag -a 0.1.1 -m "release 0.1.1 publish" master<br>
git push --tags<br>
</pre><br>
同样也需要将修复分支合并到 develop 分支<br>
<pre class="prettyprint">git checkout develop<br>
git merge --no-ff hotfix-auth<br>
git push<br>
</pre><br>
最后删除掉这个热修复分支<br>
<pre class="prettyprint">git branch -d hotfix-auth<br>
</pre><br>
<h4>主要遵循原则</h4>它基于两个长期的主要分支：<br>
<ul><li>主分支 <code class="prettyprint">master</code> 该分支包含生产代码。 该分支是稳定的发布版</li><li>开发分支 <code class="prettyprint">develop</code> 此分支包含预生产代码。所有的功能分支完成后需要合并到该分支</li></ul><br>
<br>其次在开发中还有三种短期分支：<br>
<ul><li>功能分支（feature branch）功能分支用于为即将发布的版本开发新功能。从<code class="prettyprint">develop</code>分支中检出也必须合并回 <code class="prettyprint">develop</code>。</li><li>补丁分支（hotfix branch）补丁分支 用于修复线上 bug, 从 master 分支上面检出。修复结束以后，再合并进 master 和 develop 分支</li><li>预发分支（release branch）预发布分支用于生成一个预发布版本进行测试 预发布分支是从 develop 分支上面分出来的，预发布结束以后，必须合并进 Develop 和 Master 分支。它的命名，可以采用 release-*的形式。</li></ul><br>
<br><h4>优点</h4><ul><li>整个项目生命周期内，分支状态十分干净，各个分支各司其职</li><li>分支的命名遵循系统的模式，使其更易于理解</li><li><code class="prettyprint">master</code>  和  <code class="prettyprint">develop</code>  分支分别记录发布和功能开发的历史</li><li>由于有发布分支，其他暂不发布的功能的开发不受发布的影响，可以继续提交</li><li>维护分支能快速打补丁，不影响正在开发的功能</li><li>当生产中需要多个版本时，它是理想的选择</li></ul><br>
<br><h3>缺点</h3><ul><li>较为复杂</li><li>Git 历史记录变得不可读</li><li>需要维护两个长期分支 <code class="prettyprint">master</code> 和 <code class="prettyprint">develop</code></li><li>不方便持续交付和持续集成</li></ul><br>
<br><h3>Gitlab Flow 工作流</h3>GitLab Flow 是通过创建工作流 <a href="https://about.gitlab.com/2014/09/29/gitlab-flow/">GitLab</a> 在 2014 年。它将<a href="https://en.wikipedia.org/wiki/Feature-driven_development">功能驱动的开发</a>和功能分支以及问题跟踪结合在一起。它是 Git Flow 与 GithubFflow 的综合。它吸取了两者的优点，既有适应不同开发环境的弹性，又有单一主分支的简单和便利。GitLab Flow 和 GitHub Flow 之间的最大区别是 GitLab Flow 中的环境分支支持（例如 <code class="prettyprint">staging</code> 和 <code class="prettyprint">production</code>）。<br>
<br>GitLab Flow 的最大原则叫做“上游优先”（upsteam first），即只存在一个主分支 <code class="prettyprint">master</code>，它是所有其他分支的“上游”。只有上游分支采纳的代码变化，才能应用到其他分支。<br>
<br>GitLab Flow 分成两种情形来应付不同的开发流程。<br>
<h4>持续发布</h4>对于持续发布的项目，它建议在 <code class="prettyprint">master</code> 分支以外，再建立不同的环境分支，每个环境都会有对应的分支。比如，开发环境的分支是 <code class="prettyprint">master</code>，预发环境的分支是 <code class="prettyprint">pre-production</code>，生产环境的分支是 <code class="prettyprint">production</code>。<br>
<ul><li>开发分支 <code class="prettyprint">master</code> 用于发布到测试环境，该分支为受保护的分支</li><li>预发分支 <code class="prettyprint">pre-production</code> 用于发布到预发环境，上游分支为  <code class="prettyprint">master</code></li><li>正式分支 <code class="prettyprint">production</code> 用于发布到正式环境，上游分支为 <code class="prettyprint">pre-production</code></li></ul><br>
<br>如果生产环境（production）发生错误，则要建一个新分支修改完后合并到最上游的开发分支（master）此时就是 Upstream first，且经过测试，再继续往 pre-production branch，要经过测试没有问题了才能够再往下合并到生产环境。<br>
<h4>版本发布</h4>对于“版本发布”的项目，建议的做法是每一个稳定版本，都要从 <code class="prettyprint">master</code>分支拉出一个分支，比如 <code class="prettyprint">2-3-stable</code>、<code class="prettyprint">2-4-stable</code> 等等。<br>
<br>再出现 bug 后，根据对应的 release branch 创建一个修复分支，修复工作万和城呢个后，一样要按着上游优选的原则，先合并到 master 分支，经过测试才能到才能够合并到 release 分支，并且此时要更新小版本号。<br>
<h4>工作流程示例</h4>和之前一样。首先 clone 项目到本地<br>
<br>1、当我们要实现新功能或是修复 bug 时。从 master 检出新的分支如：feature-auth<br>
<pre class="prettyprint">git checkout -b feature-auth<br>
</pre><br>
2、然后在该分支下进行工作，完成后创建提交<br>
<pre class="prettyprint">git status # 查看本地仓库的修改状态<br>
git add # 暂存文件<br>
git commit # 提交文件<br>
</pre><br>
推送代码到远程仓库<br>
<pre class="prettyprint">git push origin feature-auth<br>
</pre><br>
3、代码推送到仓库后，自定运行 GitLab CI<br>
<br>4、当我们开发完成准备合并进 master 时，在 GitLab 上创建一个 Merge Request<br>
<br>5、项目管理者进行代码审查，通过后，合并到<code class="prettyprint">master</code><br>
<br>6、运行第二次 GitLab CI<br>
<br>7、通过相应的测试后，将<code class="prettyprint">master</code>分支合并到<code class="prettyprint">stable</code>，如果是新版本则创建一个新的<code class="prettyprint">stable</code>分支<br>
<br>8、为<code class="prettyprint">stable</code>打上 tag，并进行发布<br>
<h4>主要遵循原则</h4><ol><li>使用功能分支，不直接提交（commit）到 master 分支</li><li>测试所有的提交，而不仅仅只在 master 分支上</li><li>在所有的提交上，运行所有的测试（如果你的测试时间长于 5 分钟则让它们并行）</li><li>在合并到 master 之前执行代码审查，而不是事后审查</li><li>部署是自动的，并基于分支或标签（tag）</li><li>标签（tag）是由用户设置的，而不是由 CI 创建</li><li>发布（release）是基于标签（tag）的</li><li>永远不对已推送的提交（pushed commits）进行变基（rebase）</li><li>每个人都从 master 分支开始工作，目标也是 master 分支</li><li>在 master 分支中修正错误，其次再到发布分支</li><li>提交信息（commit message）应体现意图</li></ol><br>
<br><h4>优点</h4><ul><li>它定义了如何进行持续集成和持续交付</li><li>Git 历史记录干净、易读</li></ul><br>
<br><h4>缺点</h4><ul><li>相比较于 GitHub Flow 更复杂</li><li>当需要在生产中维护多个版本时，它可能会像 Git Flow 一样变得复杂</li></ul><br>
<br><h3>总结及建议</h3>没有一个万能的适合所有项目的 Git 工作流程及分支策略，无论最终选择哪种策略，你都可以通过进一步的修改来优化它。就像前文所说的，Git 工作流程对我们提升团队生产力非常重要，在制定我们的工作流程时，应该尽量符合我们的项目具体业务需求及开发环境。但是也有如下几点小建议：<br>
<ul><li>临时分支不应该存在太久，每个分支应尽量保持精简，用完即删</li><li>工作流应该尽量简单，同时方便回滚</li><li>工作流程应该符合我们的项目发布计划</li></ul><br>
<br>参考链接：<br>
<ul><li><a href="https://www.atlassian.com/git/tutorials/comparing-workflows">atlassian comparing workflows</a></li><li><a href="https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/">What are GitLab Flow best practices?</a></li><li><a href="https://nvie.com/posts/a-successful-git-branching-model/">A successful Git branching model</a></li><li><a href="https://guides.github.com/introduction/flow/">Understanding the GitHub flow</a></li><li><a href="https://docs.gitlab.com/ee/topics/gitlab_flow.html">Introduction to GitLab Flow</a></li></ul><br>
<br>原文链接：<a href="https://www.liuxing.io/blog/git-workflow/" rel="nofollow" target="_blank">https://www.liuxing.io/blog/git-workflow/</a>
                                
                                                              
</div>
            