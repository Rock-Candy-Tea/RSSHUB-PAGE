
---
title: '在自如大前端DevOps建设中JIRA的应用'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=5580'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 23:48:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=5580'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、背景介绍</h3>
<h5 data-id="heading-1">1、什么是DevOps</h5>
<p>近年来DevOps一词在整个IT行业是火遍全球，目前也没有权威的统一定义，在不同的组件及场景也产生了各种各样对它的理解和定义，比如有人把DevOps定义为是一种模式、一种工具、一种平台、一种实践、一种文化、思想、价值观等等，从不同的角度去描绘DevOps。</p>
<p>DevOps内容非常丰富，有理论也有实践，包括组织文化、自动化、精益、反馈和分享等不同方面，是一组过程、方法与系统的统称，强调高效组织团队之间如何通过自动化的工具协作和沟通来完成软件的生命周期管理，从而更快、更频繁地交付更稳定的软件。</p>
<p>换句话说DevOps希望做到在软件产品交付过程中，通过IT工具链的打通，自动化流程使得软件构建、测试、发布更加快捷、频繁和可靠，在开发、测试和运维团队减少时间损耗，更加高效地协调工作。</p>
<h5 data-id="heading-2">2、什么是JIRA</h5>
<p>JIRA是Atlassian公司出品的一款集项目管理、任务分配、需求管理、缺陷跟踪的过程管理软件。通过JIRA系统，可以整合项目管理人员、产品人员、开发人员、测试人员、运维人员等各司其职，信息很快得到交流和反馈，通过数据准确地了解项目的开发进度、质量和状态，以及整个团队的工作效率。</p>
<h5 data-id="heading-3">3、相关建设简单介绍</h5>
<p>目前，移动端应用的研发发版流程借助于内部研发的DevOps平台进行，其中发版流程主要的几个阶段了：分支的创建、测试执行的创建、测试用例的创建、提测、测试、分支主干合并、主干分支的打包上线。JIRA作为项目管理和需求追踪工具基本贯穿于软件研发整个生命周期中，从项目的立项开始，产品需求的产出、研发任务需求、QA测试任务需求、缺陷任务需求、到最后运维上线的需求，还有到需求任务的拆解、新增小需等，每个JIRA需求经历从创建流转到最后的完成的整个工作流周期。</p>
<p>在内部DevOps建设过程中，JIRA相关的应用的也不断的完善，从手动的创建JIRA、手动去关联分支和JIRA、手动更新JIRA状态、手动关联JIRA和测试用例、测试执行等等。我们逐步系统自动化集成，规范项目管理流程、规范需求池的使用，来提高工作沟通效率、较低人为因素的影响、系统记录更客观的研发过程度量数据，提高产品的质量保证和上线交付速度。现介绍下JIRA集成中的一些总结，提供给大家使用中参考。</p>
<h3 data-id="heading-4">二、JAVA项目中JIRA的集成方法</h3>
<p>JIRA本身API非常强大，但它是一个底层的API体系，如果要开发和拓展，需要二次封装，官方提供了java客户端库，也提供了丰富的REST API调用。
####方法1、集成jira官方提供的java客户端类库jira-rest-java-client-core
第一步：maven类库引入</p>
<pre><code class="copyable"><dependency>
<groupId>com.atlassian.jira</groupId>
<artifactId>jira-rest-java-client-core</artifactId>
<version>5.2.1</version>
</dependency>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步：使用示例</p>
<pre><code class="copyable"> // 登录获取 jiraClient
 AsynchronousJiraRestClientFactory asynchronousJiraRestClientFactory = new AsynchronousJiraRestClientFactory();
 JiraRestClient jiraRestClient = asynchronousJiraRestClientFactory.createWithBasicHttpAuthentication(URI.create(jiraUrl), userName, password);

 //JIRA ISSUE获取
 IssueRestClient issueClient = jiraRestClient.getIssueClient();
 Issue issue = issueClient.getIssue(issueKey).claim();
 
 //更新jira的状态，如状态从打开修改为处理中
 jiraRestClient.getIssueClient().transition(issue, new TransitionInput(11));
 
 //Jira Issue的创建
 IssueRestClient issueClient = jiraRestClient.getIssueClient();

  IssueInputBuilder builder = new IssueInputBuilder();
  builder.setIssueTypeId(TECHNICAL_TYPE_ID);
  builder.setProjectKey(PROJECT_KEY);
  builder.setSummary(summary);
  builder.setPriorityId(priorityId);
  builder.setDescription(description);
  builder.setFieldValue("customfield_10222", ComplexIssueInputFieldValue.with("value", "技术中心"));
  builder.setFieldValue("customfield_10220", ComplexIssueInputFieldValue.with("value", "互联网产品技术平台"));
  .... //其他属性的设置

  IssueInput issueInput = builder.build();
  BasicIssue basicIssue = issueClient.createIssue(issueInput).claim();

 Issue issue = issueClient.getIssue(basicIssue.getKey()).claim();
 
 ...
 //参考API使用文档
 

  
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">方法2、集成一款更简单轻量级的java客户端类库JIRA-Client</h4>
<p>第一步：maven类库引入</p>
<pre><code class="copyable"><dependency>
  <groupId>net.rcarz</groupId>
  <artifactId>jira-client</artifactId>
  <version>0.5</version>
  <scope>compile</scope>
</dependency> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步：使用示例</p>
<pre><code class="copyable">  //连接获取
  BasicCredentials creds = new BasicCredentials(username, password);
  JiraClient jiraClient = new JiraClient(jiraUrl, creds);
  
  //获取一个Jira需求的内容详情
  Issue issue = jiraClient.getIssue(issueId);
  
  //Jira 状态更新 如从工作流程状态从“开发开发” 到 “提测，等待测试”等
  issue.transition().execute(workflow); 
  
  //更新修改jira一个字段的值 
  issue.update().field(fieldName,fieldValue).execute();
  
  //给Jira需求issue创建连接
  issue.link(oldIssue,"Relates");
  
  //为Jira Issue创建子任务 如为Issue创建开发子任务：issueType=开发子任务
   Issue subtask = Issue.create(jiraClient.getRestClient(),issue.getProject().getKey(),issueType)
            .field("parent", issue.getKey())
            .field(Field.PRIORITY,issue.getPriority())
            .field(Field.ASSIGNEE,assignee)
            .field(Field.SUMMARY, summary)
            .field("customfield_11127",customfield_11127) //研发团队
            .execute();
            
   //获取Issue某个属性的值
   CustomFieldOption customFieldOption= CustomFieldOption.get(jiraClient.getRestClient(),fieldId);
  

   //新需求Issue的创建
   Issue newIssue = jiraClient.createIssue(issueKey, issueType)
            .field(Field.SUMMARY, reqVo.getSummary())
            .field(Field.DESCRIPTION, reqVo.getDescription())
            .field("customfield_11248", customfield_11248) //所属核心聚焦目标 Json对象
            .field("customfield_11127", customfield_11127) //研发团队  Json对象
            .field("customfield_10220",customfield_10220) //需求来源部门  Json对象
            .field("customfield_11120",reqVo.getPlanDate()) //计划上线时间 
            .field("customfield_10116",reqVo.getAssignee()) //需求发起人
            .field(Field.ASSIGNEE, reqVo.getAssignee()) //经办人
            .execute();
            
            
               
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">方法3、JIRA的Rest API调用</h4>
<p>目前Jira REST API 提供与V2和V3版本，但V3版本是公共测试版本，正式版本为V2，所以在生成调用的时候参照V2版本的使用。调用接口的路径结构为：https://&#123;site-url&#125;/rest/api/2/&#123;resource-name&#125;<br>
如：Jira Issue的GET获取：https://&#123;your-jira-domain&#125;/rest/api/2/issue/&#123;issueId&#125;<br>
RestAPI调用的时候需要本地搭建Jira账号的请求Header鉴权信息。<br>
官方文档有非常详细的说明，更多内容请查看官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.atlassian.com%2Fcloud%2Fjira%2Fplatform%2Frest%2Fv2%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.atlassian.com/cloud/jira/platform/rest/v2/" ref="nofollow noopener noreferrer">developer.atlassian.com/cloud/jira/…</a></p>
<h3 data-id="heading-7">三、总结</h3>
<p>以上简单介绍了三种Jira在系统间的对接打通方式，一般普遍功能对接其实都可以满足，具体的选择要注意，一要根据具体的情况，若引入第三方库要注意版本的选择；二要相信只要Web端可以操作的功能，一定会找到相应的API操作。三具体的开发中，可能会遇到各种问题要多参阅文档、多进行单元测试、也多扩展思路。比如Jira的状态是基于工作流的，也就是说状态的更新就是工作流的流转；工作的流转是按照流程顺序，不可逆的；如果有出现工作流的反向操作，那可以通过挂起来解决。</p>
<p>DevOps的建设是组织团队内不断优化迭代的过程，不断为组织的产品输出和价值交付提供更规范、更高效、更有保障的平台和指导。JIRA在平台化的流程中自动化集成的应用，一方面，让产品、研发、测试、运维能高效的沟通协作，加速价值交付的周期；另一方面，为研发过程、交付时效、研发质量等的度量提供了更客观的的基础系统化数据。</p>
<p>以上内容如有雷同纯属巧合，感谢阅读，欢迎吐槽。</p>
<p>参考链接：<br>
1、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.atlassian.com%2Fcloud%2Fjira%2Fplatform%2Frest%2Fv2%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.atlassian.com/cloud/jira/platform/rest/v2/" ref="nofollow noopener noreferrer">developer.atlassian.com/cloud/jira/…</a><br>
2、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.atlassian.com%2Fjira-rest-java-client-api%2F2.0.0-m31%2Fjira-rest-java-client-api%2Fapidocs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.atlassian.com/jira-rest-java-client-api/2.0.0-m31/jira-rest-java-client-api/apidocs/" ref="nofollow noopener noreferrer">docs.atlassian.com/jira-rest-j…</a><br>
3、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frcarz%2Fjira-client" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rcarz/jira-client" ref="nofollow noopener noreferrer">github.com/rcarz/jira-…</a></p>
<blockquote>
<p>本文作者：自如大前端研发中心-秦小明</p>
</blockquote></div>  
</div>
            