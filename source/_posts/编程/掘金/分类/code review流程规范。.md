
---
title: 'code review流程规范。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 16:18:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image" alt="掘金引流终版.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>张宇航：微医前端技术部医保支撑组，一个不文艺的处女座程序员。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>没有无缘无故的爱，也没有无缘无故的恨，当然也没有无缘无故的 code review</p>
<h2 data-id="heading-1">为什么要 CR</h2>
<p>给大家讲个故事，“大神 A”上班时突然恼羞成怒的骂道，<strong>这是谁写的代码，没有注释啥也没有，这么明显的 bug。当时整个小组都不敢说话，慌的要死，生怕说的就是自己。领导发话：“大神 A”查下提交记录，谁提交的谁请吃饭。过了两分钟，“大神 A”：这，这</strong>是我自己一年前提交的。所以不想自己尴尬，赶紧 code review 吧</p>
<h2 data-id="heading-2">一、角色职能</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a082f511fb049589be14c0c38ba2bf1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
<strong>author 即需求开发者。要求：</strong></p>
<ol>
<li>注重注释。对复杂业务写明相应注释，commit 写名具体提交背景，便于 reviewer 理解。</li>
<li>端正心态接受他人 review。对 reviewer 给出的 comment，不要有抵触的情绪，对你觉得不合理的建议，可以委婉地进行拒绝，或者详细说明自己的看法以及原因。reviewer 持有的观点并不一定是合理的，所以 review 也是一个相互学习的过程。</li>
<li>完成 comment 修改后及时反馈。commit 提交信息备注如"reivew: xxxx"，保证复检效率。</li>
</ol>
<p><strong>reviewer 作为 cr 参与者，建议由项目责任人和项目参与者组成。要求：</strong></p>
<ol>
<li>说明 comment 等级。reviewer 对相应代码段提出评价时，需要指明对应等级，如
<ul>
<li>fix: xxxxxxx 此处需强制修改，提供修改建议</li>
<li>advise: xxxxxxx 此处主观上建议修改，不强制，可提供修改建议</li>
<li>question: xxxxxx 此处存在疑虑，需要 author 作出解释</li>
</ul>
</li>
<li>友好 comment。评价注意措辞，可以说“我们可以如何去调整修改，可能会更合适。。。”，对于比较好的代码，也应该给与足够的赞美。</li>
<li>享受 review。避免以挑毛病的心态 review，好的 reviewer 并不是以提的问题多来衡量的。跳出自己的编码风格，主动理解 author 的思路，也是一个很好的学习过程。</li>
</ol>
<h2 data-id="heading-3">二、CR 流程</h2>
<h4 data-id="heading-4">1、self-review</h4>
<ul>
<li>commit 之前要求 diff 一下，查看文件变更情况，可接着 gitk 完成。当然如果项目使用 pre-commit 关联 lint 校验，也能发现例如 debugger、console.log 之类语句。但是仍然提倡大家每次提交之前检查一下提交文件。</li>
<li>多人协作下的 commit。多人合作下的分支在合并请求时，需要关注是否带入没必要的 commit。</li>
<li>commit message。建议接入 husky、commitlint/cli 以及 commitlint/config-conventional 校验 commit message。commitlint/config-conventional 所提供的类型如
<ul>
<li>feat: 新特性</li>
<li>fix: 修改 bug</li>
<li>chore: 优化，如项目结构，依赖安装更新等</li>
<li>docs: 文档变更</li>
<li>style: 样式相关修改</li>
<li>refactor：项目重构</li>
</ul>
</li>
</ul>
<p>此目的为了进一步增加 commit message 信息量，帮助 reviewer 以及自己更有效的了解 commit 内容。</p>
<h4 data-id="heading-5">2、CR</h4>
<ol>
<li>提测时发起 cr，需求任务关联 reviewer。提供合并请求，借助 gitlab/sourcetree/vscode gitlens 等工具。reviewer 结束后给与反馈</li>
<li>针对 reviewer 提出的建议修改之后，commit message 注明类似'review fix'相关信息，便于 reviewer 复检。</li>
<li>紧急需求，特事特办，跳过 cr 环节，事后 review。</li>
</ol>
<h2 data-id="heading-6">三、CR 标准</h2>
<ol>
<li>不纠结编码风格。编码风格交给 eslint/tslint/stylelint</li>
<li>代码性能。大数据处理、重复渲染等</li>
<li>代码注释。字段注释、文档注释等</li>
<li>代码可读性。过多嵌套、低效冗余代码、功能独立、可读性变量方法命名等</li>
<li>代码可扩展性。功能方法设计是否合理、模块拆分等</li>
<li>控制 review 时间成本。reviewer 尽量由项目责任人组成，关注代码逻辑，无需逐字逐句理解。</li>
</ol>
<h2 data-id="heading-7">四、最后</h2>
<p>总的来说，cr 并不是一个找 bug 挑毛病的过程，更不会降低整体开发效率。其目的是为了保证项目的规范性，使得其他开发人员在项目扩展和维护时节省更多的时间和精力。当然 cr 环节需要团队每一个成员去推动，只有每一个人都认可且参与进来，才能发挥 cr 的最大价值。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44a4781f55844122bc07e0c5bc017d16~tplv-k3u1fbpfcp-watermark.image" alt="f5e284a8e87e4340b5f20e9c88fb2777_tplv-k3u1fbpfcp-zoom-1.gif" loading="lazy" referrerpolicy="no-referrer">
最后安利一波本人开发 vscode 小插件搭配 gitlab 分支 review，主要流程是点击按钮发起合并请求，自动生成 mr 链接，并发送至企业微信通知相关责任人开始 review。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/192a908c8d534790b0668ea2fbb581bc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            