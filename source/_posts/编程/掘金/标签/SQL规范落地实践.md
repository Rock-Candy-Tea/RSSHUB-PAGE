
---
title: 'SQL规范落地实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc77061cdbfd4758baf3a4e81a7a41a2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 08:01:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc77061cdbfd4758baf3a4e81a7a41a2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<p>本文由<strong>707</strong>同学供稿~</p>
<h1 data-id="heading-0">1.概述</h1>
<p>数据库在各类生产系统中是不可或缺的中间件，SQL代码作为操作数据库的标准语法，在日常开发中使用比例非常高，几乎每个批次都会有产品涉及，但各开发人员对SQL开发技能的掌握程度参差不齐。</p>
<p>为了规避开发技能不足，而引发SQL质量问题的风险，在最大程度上规范开发方法，由数据库专家团队从历史经验和业界优秀实践中总结出一套SQL代码开发规范。</p>
<p>然而，无法落地的规范，只能是空中楼阁，为了能够让规范顺利落地，我们通过将规范内化在工具中，将一条条规范条文具象化、可验证化，以检查开发人员提交的SQL代码质量。</p>
<h1 data-id="heading-1">2.规范</h1>
<h3 data-id="heading-2">2.1 整体介绍</h3>
<p>为了更好地指导产品SQL设计及开发，避免不恰当的设计、开发带来问题和隐患，同时为了提升开发人员对SQL相关知识的掌握程度，制定了若干SQL规范。</p>
<p>本规范分为SQL设计规范和SQL开发规范两个部分。SQL设计规范重点关注在设计阶段需要考虑的库、表、字段、索引设计，通过充分设计降低后续工程阶段正向及反向实施成本。SQL开发规范重点关注编码、DDL、DML、查询优化，通过明确的规则指导编写合理、高效的SQL语句。</p>
<p>本实践落地的SQL规范为开发规范，具体规范如下，包含DML、DQL和DDL，并且规范分为三个级别：强制、推荐和参考，强制表示必须按照规范实现，推荐表示建议按照规范实现，参考表示仅提供参考。</p>
<h3 data-id="heading-3">2.2 DML与DQL规范示例</h3>
<p>**【强制】**SQL关键字大写</p>
<p>**【强制】**INSERT语句必须要插入的字段名称</p>
<p>**【强制】**数据行删除/更新使用delete/update时，必须带上WHERE子句</p>
<p>**【强制】**禁止在UPDATE语句中，将“,”写成AND</p>
<p>**【推荐】**如果需要清除全表数据，建议使用TRUNCATE TABLE删除所有的行</p>
<p>**【推荐】**避免使用REPLACE。先采用SELECT判断是否存在记录，然后再考虑INSERT或UPDATE</p>
<p>**【参考】**如无必要锁定数据，则应避免使用FOR UPDATE</p>
<p>**【强制】**禁止使用SELECT * 查询</p>
<p>**【强制】**WHERE 条件中的过滤条件字段上严禁使用任何函数,包括数据类型转换函数</p>
<p>**【强制】**多表关联查询时，避免使用非索引字段作为关联条件</p>
<p>**【强制】**禁止使用ORDER BY RAND()</p>
<p>**【强制】**进行模糊查询时，避免使用左模糊或者全模糊匹配。根据最左前缀原则合理安排查询条件</p>
<p>**【推荐】**避免使用COUNT(*)作为查询字段</p>
<p>**【推荐】**相同字段的OR条件大于3个，建议使用IN代替</p>
<p>**【推荐】**不同字段的OR条件大于3个，建议使用使用UNION ALL代替</p>
<p>**【推荐】**尽量避免在SELECT子句中使用子查询，替换为连接查询</p>
<p>**【推荐】**考虑使用IN替代EXISTS做嵌套查询</p>
<p>**【推荐】**必须进行表关联查询时，控制关联表的个数不超过两个</p>
<p>**【推荐】**外连接的 SQL 语句,建议一律写成LEFT JOIN（左侧为主表），而不要使用 RIGHT JOIN</p>
<p>**【推荐】**对MIN(), MAX()等聚合函数，建议利用数据的有序性配合LIMIT 1将SQL等价转化</p>
<p>**【推荐】**使用WHERE子句代替HAVING子句</p>
<p>**【强制】**分页查询语句全部都需要带有排序条件，除非业务方明确要求不要使用任何排序来随机展示数据</p>
<p>**【强制】**多表 JOIN 的分页语句，如果过滤条件在单个表上，先利用索引在子查询中通过分页限定数据范围，再 JOIN</p>
<p>**【推荐】**大数据量分页查询时，避免直接使用数据库提供的分页命令LIMIT m,n</p>
<p>**【强制】**SQL语法错误导致的异常</p>
<h3 data-id="heading-4">2.3 DDL规范示例</h3>
<p>**【强制】**避免使用存储过程、触发器、函数等，容易将业务逻辑和数据库耦合在一起；</p>
<p>**【强制】**所有的数据库对象命名，只使用小写字母、数字和下划线的组合，并以字母开头。</p>
<p>**【强制】**禁止使用SQL关键字进行数据库对象命名。</p>
<p>**【强制】**所有的数据库对象命名，长度不要超过32个字符。</p>
<p>**【推荐】**采用如下规则进行索引命名：</p>
<p>非唯一索引按照“idx_字段名称_字段名称[_字段名]”进行命名；</p>
<p>唯一索引按照“uk_字段名称_字段名称[_字段名]”进行命名；</p>
<p>主键按照：pk_表名称。</p>
<p>**【强制】**明确指定数据库默认的字符集和校验规则；</p>
<p>**【推荐】**所有表统一使用utf8字符集，排序规则采用utf8_general_ci。特殊情况如：需要存Emoji表情，则可选utf8mb4，校对规则采用对应的utf8mb4_general_ci。</p>
<p>**【参考】**控制单表字段个数不要超过50个。</p>
<p>**【强制】**存储TEXT类型的字段时，独立出来一张表，用主键来对应，避免影响其它字段索引效率。</p>
<p>**【推荐】**建表必备三个字段：id, create_time, update_time.</p>
<p>**【推荐】**如果可能，字段尽量使用NOT NULL属性，并且设置默认值。</p>
<p>**【推荐】**如果变长字符型长度超过2000，采用TEXT类型。</p>
<p>**【强制】**InnoDB引擎表必须设置主键。</p>
<p>**【强制】**禁止使用外键。</p>
<p>**【强制】**在varchar字段上建立索引时，必须指定索引长度，没必要对全字段建立索引，根据实际文本区分度决定索引长度。</p>
<p>**【推荐】**采用自增整型字段作为InnoDB引擎表的主键。</p>
<p>**【推荐】**避免冗余索引：避免在主键列上重复建立索引；根据最左前缀原则避免重复索引。</p>
<p>**【强制】**对表的多次ALTER操作合并为一次操作</p>
<h1 data-id="heading-5">3.检查规范落地</h1>
<h3 data-id="heading-6">3.1 落地方式</h3>
<p>在设计过程中，考虑到以工具来实现，既能让开发环境本地自测，也可以通过DevOps平台自动回归检查，并且尽量对工程减少入侵。故采用Maven插件的形式来提供支持，对原工程业务代码无任何入侵，且插件只在编译构建阶段生效，不会对服务的执行产生任何影响。该方式无论在本地配置还是在DevOps平台配置均可方便使用，避免对开发人员造成额外的工作负担。</p>
<h3 data-id="heading-7">3.2 架构设计</h3>
<p>本SQL检查工具针对使用Mybatis框架的工程，架构由两部分组成，分别是核心模块和插件模块，将上层插件与核心拆分开，而非形成单体结构，可最大化增加可扩展性。该工具的核心设计思路与核心代码以分享过，详见<a href="https://juejin.cn/post/6947125430977560606" target="_blank" title="https://juejin.cn/post/6947125430977560606">动手撸一个SQL规范检查工具</a>。</p>
<p><strong><strong>核心部分</strong></strong>负责SQL的解析，最重要的是DDL、DML和DQL三种类型SQL规则，根据前文中的规范编写落地为对应的语法规则，一条规则对应一个类文件，若规则有扩充可便捷地向核心模块追加。</p>
<p><strong><strong>插件部分</strong></strong>目前为Maven形式，以核心作为支撑，插件在编译阶段运行时会调起核心模块，依次检查所有的规则，未来可根据需求扩展为其他形式的插件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc77061cdbfd4758baf3a4e81a7a41a2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/7001511601786322952" loading="lazy" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-8">3.3 执行逻辑</h3>
<p><strong><strong>收集SQL语句</strong></strong>：扫描代码中Mybatis相关的mapper配置文件，比如位于资源文件夹中的配置文件resources/mapper/*.xml，识别出所有SQL语句，供后续进行分析。</p>
<p><strong><strong>语法分析</strong></strong>：根据SQL语法规则，对SQL语句进行语法分析，提取出SQL语句各关键字元素，并进行中间结果分类保存，再做进一步分析。</p>
<p><strong><strong>规范检查</strong></strong>：</p>
<p>1.静态检查</p>
<p>根据预先设计好的语法检查规则，对SQL语句进行静态代码检查，逐条进行分析扫描，得到每条规则的评判结果，进行记录。</p>
<p>2.动态检查</p>
<p>有一些规则依赖于真实的数据库，仅凭SQL静态检查无法完全覆盖，故在仿真生产环境的镜像库，对SQL语句进行重放，识别对数据库表记录增删改查操作耗时时长，识别慢SQL。收集SQL执行计划，分析是否为最优执行计划。</p>
<h3 data-id="heading-9">3.4 报告展示</h3>
<p>规范检测很重要，但是结果的展示也同样重要，具有一种设计优良的可视化展示形式是非常重要的。本工具提供了多种展示形式，包括终端展示、Json报文结构展示、Html页面展示三种，并且提供了方便的可扩展点，通过开发新的Appender即可添加新的展示形式。报告结果中会有所有检测出的漏洞问题，以及解决方案，用户可以根据提示对SQL进行整改。</p>
<p>此外，还提供了相应的仪表盘网站，页面中可展示所有产品的检测结果汇总和详情。可通过该站查看所有批次缺陷趋势，某个批次各产品的缺陷分布，某个产品的各批次缺陷数量趋势，以及某批次某产品各种缺陷类型的分布情况。用户通过该网站可查看各产品缺陷增长和缺陷修复情况，并可以按照各批次和各产品筛选缺陷情况，从多个维度监测各产品SQL规范情况。从各产品的排名可以起到正向的督促监督作用，有对比竞争能够极大激发大家修改漏洞的欲望，促进SQL质量的稳步提升。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f87607dce8554fc7a5b11c057b217882~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">​3.5 DevOps自动化</h3>
<p>SQL检查是一个持续的过程，需要在开发过程中不断地进行，我们可以通过CI进行集成，在执行Maven构建的命令中添加SQL检查插件的执行命令，按照一定的构建规则，可以持续向仪表盘上推送数据。这样就形成一个持续不断的流式SQL检查结果，可实时统计出缺陷情况。</p>
<h1 data-id="heading-11">4. 总结</h1>
<p>通过规范的制定、规范的开发、规范的结果展示和规范的自动化检查，一系列的实践成功将SQL规范落地，本规范的落地标志着这种方式的探索初见成效，是一种可行的方案。SQL规范仅仅是一个开始，未来更多的规范同样可以以这种方式落地，并最终开花结果。</p>
<p>​</p></div>  
</div>
            