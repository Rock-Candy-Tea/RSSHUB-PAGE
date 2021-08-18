
---
title: 'Jenkins Pipeline 结合 Gitlab 实现 Node 项目自动构建'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed5238ded9644e02a07cca436c68dcd6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 02:10:25 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed5238ded9644e02a07cca436c68dcd6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>Jenkins</code> 是什么？</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jenkins.io%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jenkins.io/zh/" ref="nofollow noopener noreferrer">Jenkins</a> 是一款开源 <code>CI&CD</code> 软件，用于自动化各种任务，包括构建、测试和部署软件。</p>
<p>本博文将讲解自动构建的部分。</p>
<p><code>Jenkins</code> 的安装可参考文章<a href="https://juejin.cn/post/6844903992833605640" target="_blank" title="https://juejin.cn/post/6844903992833605640">从零开始搭建JENKINS+GITHUB持续集成环境【多图】</a>。</p>
<p>讲解的内容包括：</p>
<ul>
<li>
<p>新建流水线</p>
</li>
<li>
<p>Jenkins 配置</p>
</li>
<li>
<p>Gitlab 配置</p>
</li>
</ul>
<p>直接进入主题～</p>
<h3 data-id="heading-0">新建流水线</h3>
<blockquote>
<p>Dashboard -> 新建任务</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed5238ded9644e02a07cca436c68dcd6~tplv-k3u1fbpfcp-watermark.image" alt="create_a_pipeline.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>✅ 建议：任务名称填写与仓库名称一致，一一对应方便查找任务。</p>
<p>新建完成任务之后，会自动跳转到该任务的配置页面。</p>
<h3 data-id="heading-1">Jenkins 配置</h3>
<p>这里的配置，去要做一下细分。</p>
<h4 data-id="heading-2">公共配置</h4>
<p><strong>系统配置</strong></p>
<blockquote>
<p>Dashboard -> 系统管理 -> 系统配置 -> Gitlab</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4bfaa5f5a0945558c7d4b221d50fa03~tplv-k3u1fbpfcp-watermark.image" alt="gitlab_setting.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Connection name 表示链接的名称，这里我填了 Gitlab ，后面要用到</li>
<li>Gitlab host URL 表示你 Gitlab 的域名链接</li>
<li>Credentials 凭证
<ul>
<li>凭证的获取需点击“添加”进入</li>
<li>具体的生成步骤 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fuser%2Fprofile%2Fpersonal_access_tokens.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html" ref="nofollow noopener noreferrer">personal_access_tokens</a></li>
</ul>
</li>
</ul>
<p><strong>全局工具配置</strong></p>
<blockquote>
<p>Dashboard -> 系统管理 -> 全局工具配置 - NodeJS</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c29d0fc07834c8a8ce4516bea16ef4a~tplv-k3u1fbpfcp-watermark.image" alt="install_node.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>别名这里起了 <code>nodejs</code> ，在后面写 Jenkinsfile 的时候会用到</li>
<li>安装的版本当前的稳定版即可，文章发表时，<code>NodeJS</code> 的稳定版是 <code>NodeJS 14.17.5</code></li>
</ul>
<h4 data-id="heading-3">任务配置</h4>
<p>如果按照正常操作，新建完成任务之后，会自动跳转到该操纵页面。当然，你还可以通过下面的操作进入：</p>
<blockquote>
<p>Dashboard -> PipelineTask -> 配置</p>
</blockquote>
<p>只需要留意下面的内容即可：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/438ffa26757b49e4bfe03f96a95f6265~tplv-k3u1fbpfcp-watermark.image" alt="step_general.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>General 板块
<ul>
<li>描述表明这个任务是干什么的，可有可无</li>
<li>GitLab Connection 选择我们在“系统配置”中设定好的选项</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f336ca4c34674b8f908c79d4fb722bb7~tplv-k3u1fbpfcp-watermark.image" alt="step_trigger.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>构建触发器板块
<ul>
<li>只要勾选 <code>Build when a change is pushed to GitLab. GitLab webhook URL: http://localhost:8080/project/PipelineTask</code> 即可</li>
</ul>
</li>
</ul>
<p>🀄️ 这里有两点后面需要用到（上面截图并非完整，自行体验）：</p>
<ol>
<li>GitLab webhook URL</li>
<li>Secret token （点击“高级” -> Generate 按钮生成）</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/032c12a0f1b446c18ebf2ec115173566~tplv-k3u1fbpfcp-watermark.image" alt="step_pipeline_scm_choose.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>流水线模块
<ul>
<li>定义下拉框选择 Pipeline script from SCM ，因为我们是通过项目的 <code>Jenkinsfile</code> 进行构建的</li>
<li>SCM 选择 Git</li>
<li>Repository URL 填写项目的仓库地址，比如 <code>https://gitlab.mydomain.com/apps/pipeline_task.git</code></li>
<li>Credentials 是凭证，你 GitLab 的账号密码</li>
</ul>
</li>
</ul>
<h3 data-id="heading-4">Gitlab 配置</h3>
<p><code>Gitlab</code> 上做一个关联，与 <code>Jenkins</code> 关联上，当仓库 <code>push</code> 操作的时候，<code>Jenkins</code> 上自动构建项目。</p>
<p>🀄️ PS：当然 <code>push</code> 操作只是其中一种情况，还可以打标签之类的</p>
<blockquote>
<p>进入你仓库相应项目 -> Settings -> Integrations</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44e50e0225284bd79ac9050c4ae94b37~tplv-k3u1fbpfcp-watermark.image" alt="gitlab_webhook.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>URL 对应上面 Jenkins 触发器上设定的 GitLab webhook URL</li>
<li>Secret Token 对应上面 Jenkins 触发器上生成的 Secret token</li>
</ul>
<p>添加了 <code>Webhook</code> 之后可以进行测试，查看是否通了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df3c3a8bfb8345228bb22de1edf30ea6~tplv-k3u1fbpfcp-watermark.image" alt="gitlab_test_push.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果测试通过，会出现 <code>Hook executed successfully: HTTP 200</code> 的提示。</p>
<p>在触发构建之前，我们在对应仓库根目录下写个简单的脚本 <code>Jenkinsfile</code> ：</p>
<pre><code class="copyable">pipeline &#123;
    agent any
    
    tools &#123; 
        nodejs "nodejs" 
    &#125;
    
    stages &#123;
        stage('Dependency') &#123;
            steps &#123;
                sh 'npm install'
            &#125;
        &#125;
        stage('Build') &#123; 
            steps &#123;
                sh 'npm run clean' 
                sh 'npm run build' 
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目每次进行 <code>push</code> 的时候，就会自动构建，构建的步骤按照 <code>Jenkinsfile</code> 设定的走。</p>
<p>【完】</p></div>  
</div>
            