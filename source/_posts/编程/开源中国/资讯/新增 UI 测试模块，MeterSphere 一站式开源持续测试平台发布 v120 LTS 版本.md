
---
title: '新增 UI 测试模块，MeterSphere 一站式开源持续测试平台发布 v1.20 LTS 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f37876cb3f1700b482df0ee827b3fac8fee.png'
author: 开源中国
comments: false
date: Thu, 05 May 2022 15:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f37876cb3f1700b482df0ee827b3fac8fee.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="824" src="https://oscimg.oschina.net/oscnet/up-f37876cb3f1700b482df0ee827b3fac8fee.png" width="1696" referrerpolicy="no-referrer"></p> 
<div style="margin-left:auto; margin-right:auto; text-align:start"> 
 <div> 
  <div> 
   <p style="margin-left:0; margin-right:0">2022年5月5日，<strong>MeterSphere一站式开源持续测试平台正式发布v1.20 LTS版本</strong>。这是继2021年5月发布v1.10 LTS版本后，MeterSphere开源项目发布的第二个LTS（Long Term Support）版本。</p> 
   <p style="margin-left:0; margin-right:0">MeterSphere开源项目组将对MeterSphere v1.20 LTS版本用户提供长期支持，在主线功能版本的基础之上，按需发布LTS版本的问题修复更新，为用户提供更加稳定和高质量的软件使用体验。</p> 
   <p style="margin-left:0; margin-right:0">MeterSphere v1.20 LTS版本深入践行“一站式持续测试平台”的设计理念，<strong>新增了UI测试模块（X-Pack增强包内）</strong>，实现了对测试跟踪、接口测试、UI测试和性能测试的一站式覆盖。</p> 
   <p style="margin-left:0; margin-right:0">至此，<strong>MeterSphere开源持续测试平台已经完整提供测试跟踪、接口测试、UI测试、性能测试，以及团队协作与融入DevOps五大核心功能</strong>。而在经历了20个版本的持续迭代后，MeterSphere开源项目组对MeterSphere v1.20 LTS版本的系统性能进行深度优化，软件运行稳定性显著提升，将为广大用户提供更加稳定和流畅的使用体验。</p> 
   <p style="margin-left:0; margin-right:0">MeterSphere v1.20 LTS版本在功能性的上升级包括：在测试跟踪模块，<strong>MeterSphere新增测试计划“已归档”状态，同时支持批量运行测试计划功能</strong>；在接口测试模块，<strong>场景自动化支持多数据源环境平滑切换，以及新增自定义“误报库”匹配逻辑功能</strong>；在系统设置模块，<strong>增加项目级别的配额管理功能</strong>。</p> 
   <p style="margin-left:0; margin-right:0">MeterSphere v1.20 LTS版本在系统性能优化方面的工作包括：在测试计划执行效率方面，<strong>优化了入库存储机制以及执行节点轮询算法</strong>，以满足企业大数据量且高频率的自动化测试执行需求；<strong>对页面表格组件的针对性优化，重点解决了关联大批量测试用例的页面卡顿现象</strong>，有效提升批量处理列表数据的响应速度。</p> 
   <h2 style="margin-left:0; margin-right:0">新增功能</h2> 
   <p style="margin-left:0; margin-right:0"><strong>■ 新增UI测试模块（X-Pack增强包内）</strong></p> 
   <p style="margin-left:0; margin-right:0">MeterSphere UI测试模块的设计理念是基于POM（Page Object Model）页面对象模型，将页面定位和业务操作分开，分离了测试对象和测试脚本，以解决前端UI变化频繁导致测试脚本维护成本高的问题。在具体实现上，我们选用了Selenium这一使用最广泛的开源浏览器自动化方案，并且支持直接导入Selenium IDE中的测试脚本。</p> 
   <p style="margin-left:0; margin-right:0">MeterSphere的UI测试模块包含元素库、UI自动化、测试报告三大部分。</p> 
   <p><img src="https://pic4.zhimg.com/80/v2-e7d176b336e9ed606247c4289ccdf3e7_1440w.jpg" width="2870" referrerpolicy="no-referrer"></p> 
   <p style="margin-left:0; margin-right:0"><strong>元素库：</strong>集中管理页面元素，实现“一处维护，处处运行”；</p> 
   <p><img src="https://pic1.zhimg.com/80/v2-ce77017c2635eb45ac976f2c62f227ec_1440w.jpg" referrerpolicy="no-referrer"></p> 
   <p style="margin-left:0; margin-right:0"><strong>UI自动化：</strong>“搭积木”式的场景编排能力，复用性强，有效提升脚本编写效率；</p> 
   <p><img src="https://pic4.zhimg.com/80/v2-a1c38193f4cfba3b188ee0a22d4fad57_1440w.jpg" width="2878" referrerpolicy="no-referrer"></p> 
   <p style="margin-left:0; margin-right:0"><strong>测试报告：</strong>可视化的运行报告，提供执行日志、错误截图，有效提升问题定位以及分析效率。</p> 
   <p><img src="https://pic3.zhimg.com/80/v2-27a14345392e7b25e7ceb4d0285c2912_1440w.jpg" width="2844" referrerpolicy="no-referrer"></p> 
   <p style="margin-left:0; margin-right:0"><strong>■ 新增测试计划“已归档”状态</strong></p> 
   <p style="margin-left:0; margin-right:0">MeterSphere v1.20 LTS版本中针对测试计划状态新增了“已归档“状态标签，用户可以通过更新状态对处理完的测试计划进行归档管理，测试计划列表默认展示未归档的测试计划。</p> 
   <p><img src="https://pic1.zhimg.com/80/v2-310fc0814a7b968a2cea8ac034fd7090_1440w.jpg" width="2878" referrerpolicy="no-referrer"></p> 
   <p><img src="https://pic2.zhimg.com/80/v2-801966b3e7e0d1f0756714ddfac62ea1_1440w.jpg" width="2874" referrerpolicy="no-referrer"></p> 
   <p style="margin-left:0; margin-right:0"><strong>■ 新增自定义“误报库”匹配逻辑功能（X-Pack增强包内）</strong></p> 
   <p style="margin-left:0; margin-right:0">在用户实际测试的过程中，可能会遇到一些因网络异常、环境未就绪等非应用原因导致的失败。针对这些特殊情况，MeterSphere v1.20 LTS版本增加了误报标记功能，用户可以根据自身需求配置自己的误报库规则，当请求结果与某条误报规则匹配时便会被标记为“误报”状态。</p> 
   <p style="margin-left:0; margin-right:0">在MeterSphere v1.20 LTS版本中，我们对请求同时包含多个断言结果的处理方案进行了开放式处理，用户可以根据自身需要对误报结果进行升级（处理为失败）和降级（处理为成功）处理。</p> 
   <p><img src="https://pic4.zhimg.com/80/v2-b9395f3e9436e9d8efcdc80cd7b5cde3_1440w.jpg" width="2862" referrerpolicy="no-referrer"></p> 
   <p style="margin-left:0; margin-right:0">除了上述提到的新增功能外，MeterSphere v1.20 LTS版本还包含很多其他功能的新增和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
   <h2 style="margin-left:0; margin-right:0">功能优化</h2> 
   <p style="margin-left:0; margin-right:0">■ 测试跟踪：新增批量运行测试计划功能；</p> 
   <p style="margin-left:0; margin-right:0">■ 测试跟踪：测试用例页面的UI优化，方便自定义字段更好地展示；</p> 
   <p style="margin-left:0; margin-right:0">■ 测试跟踪：测试计划执行效率优化；</p> 
   <p style="margin-left:0; margin-right:0">■ 测试跟踪（X-Pack增强包内）：第三方平台缺陷支持全量同步；</p> 
   <p style="margin-left:0; margin-right:0">■ 接口测试：接口定义创建新版本时支持复制Case和Mock数据；</p> 
   <p style="margin-left:0; margin-right:0">■ 接口测试：接口自动化切换运行环境支持多数据源平滑切换（数据源名称需一致）；</p> 
   <p style="margin-left:0; margin-right:0">■ 接口测试：接口自动化创建定时任务增加运行环境校验；</p> 
   <p style="margin-left:0; margin-right:0">■ 接口测试：接口调试响应速度优化；</p> 
   <p style="margin-left:0; margin-right:0">■ 接口测试（X-Pack增强包内）：MQTT Sub支持匹配消息内容结束接收；</p> 
   <p style="margin-left:0; margin-right:0">■ 系统设置：邮件设置增加指定发件人功能；</p> 
   <p style="margin-left:0; margin-right:0">■ 系统设置：新增项目级别的配额管理。</p> 
   <h2 style="margin-left:0; margin-right:0">Bug修复</h2> 
   <p style="margin-left:0; margin-right:0">■ fix（测试跟踪）：修复通过功能用例模板上传的用例（标签中含有换行）会导致用例名称和内容是空的的问题（GitHub #12826）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（测试跟踪）：修复MQTT接口自动化中修改步骤名字后，点击调试和下拉小箭头，修改内容不生效的问题（GitHub #12457）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（测试跟踪）：修复“多个功能测试用例关联同一个场景C，其他用例关联场景用例时可见重复的场景C”的问题（GitHub #12708）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（测试跟踪）：修复对接禅道企业版时，缺陷模板中自定义字段的末尾如果有空格会导致此自定义字段无法传递给禅道的问题（GitHub #12367）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（测试跟踪）：修复脑图新增标题后，点击“保存”按钮，在设置为用例后多次点击“保存”按钮，新增的用例出现丢失的问题（GitHub #12143）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（接口测试）：Postman导入的API中，如果在Path中包含有变量，导入后在Path中存在“$&#123;xx&#125;"，修改成“&#123;xx&#125;”后无法编辑。本版本对该问题加以修复（GitHub #13042） ；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（接口测试）：修复Swagger 2.0的脚本导入到MeterSphere后，响应内容状态码显示错误的问题（GitHub #13037）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（接口测试）：修复添加用例至公共用例库后，对用例库中该用例进行编辑并保存时公共用例库中添加的用例被自动移除的问题（GitHub #13004）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（接口测试）：修复CSV文件内引号获取不准确的问题（GitHub #12920）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（接口测试）：修复Mock完成设置后执行，响应结果不是Mock设置里响应结果的问题（GitHub #12899）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（接口测试）：修复MeterSphere v1.19.3版本中，断言的启动和关闭按钮保存后未生效的问题（GitHub #12904）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（接口测试）：编辑使用接口用例时，ESB格式的TCP请求参数显示不全的问题（GitHub #12778）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（性能测试）：修复单接口用例转换为性能测试用例时，请求统计中的用例名称建议显示为原单接口用例名称的问题（GitHub #11743）；</p> 
   <p style="margin-left:0; margin-right:0">■ fix（系统设置）：修改脑图模式编写的用例，保存成功后查看操作日志记录异常的问题（GitHub #12099）。</p> 
   <p><img src="https://pic3.zhimg.com/80/v2-c4516f6f9d5a47de4829b64b382be272_1440w.jpg" width="658" referrerpolicy="no-referrer"></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            