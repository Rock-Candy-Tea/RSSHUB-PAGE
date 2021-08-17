
---
title: 'PRD：SaaS平台OA系统迭代需求文档'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/8FmiavlufhDjXrB98QPC.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 17 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/8FmiavlufhDjXrB98QPC.jpg'
---

<div>   
<blockquote><p>编辑导语：审批系统是企业中常用的系统，那么，应该如何进行规划和设计？也许你需要一份需求文档来帮助梳理用户需求，清晰目标与流程规划。本篇文章里，作者结合实际案例，梳理了一份OA系统迭代升级的需求文档，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5062133 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/8FmiavlufhDjXrB98QPC.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>本文为OA系统依照客户需求进行迭代升级的需求文档。文章共分五个章节就新功能进行阐述，希望对您有所帮助。</p>
<h2 id="toc-1">一、修订记录</h2>
<p><img data-action="zoom" class="size-full wp-image-5062025 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Kh2rsZm1g6XsoVLF8Kyh.png" alt width="529" height="119" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、需求背景与目标</h2>
<h3>项目背景与目标</h3>
<p>目前SaaS背景：现有的SaaS功能，SaaS系统已有发票的验真、结构化处理发票的数据、发票认证、抵扣等功能。</p>
<p>目标客户背景：客户为一家传统的石油国企，现在客户员工有几千人，很多都是一线员工，且财务平时跟报销发起人经常不在一起办公，需要邮寄签收材料，现在都是线下多部门处理，效率低，管理比较混乱。</p>
<p>目标：建立系统型报销流程，减少报销流程复杂度，帮助客户提高工作效率。</p>
<p>任务：在现有基础上增加财务审批的功能。</p>
<h2 id="toc-3">三、主要流程与状态机</h2>
<h3>1. 流程图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/b4kadxqNIkMsakGwNYZF.png" alt width="819" height="610" referrerpolicy="no-referrer"></p>
<h3>2. 状态机</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/9AsNAylFI1GEKFu98Z9v.png" alt width="816" height="614" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、需求列表</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/v56PgyQAfBJ1IHs9Dgze.png" alt width="592" height="290" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、功能详细逻辑</h2>
<h3>1. APP端</h3>
<p><strong>1）通用页面设置</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/AZ32rfOmoVwzmDOBiIPc.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="441" height="384" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">初始页（选择职级及所在部门）</p>
<p>这两个界面为用户注册成功并登录后的初始界面，两个界面按照用户选择情况递进，作用在于从选项区别各个用户之后的工作界面，避免工作界面程序冗余。</p>
<p>两个界面仅出现于新用户注册之后，后期职能发生更改需要到其他设置中进行切换。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/0bbj0k764UMn8HdyJyM1.png" alt width="804" height="391" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">APP主界面、更多菜单导航栏界面、审批导航栏界面</p>
<p>点击主页面的【更多】按钮，从屏幕左端向右滑出扩展菜单栏，首排第一个功能设置为【审批】，点击【审批】，进入审批项目详情页。</p>
<p>进入审批详情页后，第一排为各种审批申请的通用功能，分别为【提交申请】、【审批事项】、【抄送】和【归档】，为企业所有员工通用界面，且跳转至【审批】界面后，APP显示页面为【提交申请】主页面，下方为所有申请事项列表。</p>
<p>其中，本次迭代主要内容是优化APP端的财务类的【费用报销】功能­。</p>
<p><strong>2）各版本操作设置</strong></p>
<p><strong>① 员工版审批设置</strong></p>
<p><strong>主要页面设置及申请操作：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/cVGZwwUCLmh5ujDfSShY.png" alt width="796" height="388" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">审批主页面与选择申请费用报销后进入的费用报销填写页面</p>
<p><strong>员工财务报销操作：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/wdxqhOVD2kMKZ44JePos.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="667" height="392" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">审批页面中，【审批事项】页面、【抄送记录】页面及【归档记录】页面显示内容</p>
<p>单击【费用报销】，进入费用报销详情页，项目选择选择参与的项目（项目信息录入工作由项目负责人操作）；报销类型包括但不限于差旅费、餐费、团建费等，内容描述为该项目报销内容详情；报销金额输入需要报销的金额；图片为上传纸质发票，上传电子发票即上传电子档票据（支持PNG、JPG、PDF等格式）。</p>
<p>用户点击【审批人】栏中添加符号，跳转至通讯录选择财务业务员；【抄送】栏选择申请抄送人；保存草稿为暂存该申请，【提交】为提交给上一级审批人。</p>
<ul>
<li>【审批事项】中，普通员工可以查看自己的历史审批记录；</li>
<li>【抄送记录】为将自己的申请抄送别人的记录；</li>
<li>【归档记录】为审批结束后，自己的申请归档记录。</li>
</ul>
<p><strong>流程查看：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/rnYXYHQIBgPyyXFfOQem.png" alt width="277" height="490" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/GgUnvK0h5HzvDixX2m3Y.png" alt width="804" height="457" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/kOFa1G8yWCwSve204IBa.png" alt width="536" height="474" referrerpolicy="no-referrer"></p>
<ol>
<li>第一张为【审批事项】主页面；</li>
<li>第二排分别为“业务员审核中”、“财务审核中”及“审批通过”页面；</li>
<li>第三排为“业务员”及“财务”驳回页面。</li>
</ol>
<p>员工查看流程界面：</p>
<p>提交申请后可在【审批详情】页面中看到每个申请的进度（审批人、审批时间以及申请的信息），选择【存储为草稿】即将审核过程暂存至草稿箱；【撤回】为撤回申请；【修改】为修改申请，且不管申请推到哪步流程，选择【修改】并【重新提交】申请后，该申请转变为“新申请”并重复最初步骤（申请跳转至业务员审批）。</p>
<p><strong>修改申请：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Lpn5LPHuo8V9JQMCnYCd.png" alt width="536" height="436" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">员工修改信息界面</p>
<p>与申请界面保持一致，最后的【提交】按钮变为【再次提交】，后台进行提次数数据记录。</p>
<p><strong>② 职能部门（业务员&财务）版审批</strong></p>
<p><strong>业务员主要页面设置及审批操作：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/TcPphE9me8XviY8WZBYG.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="803" height="399" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">【审批事项】中，【审批中】、【已审批】和【申请记录】页面</p>
<p style="text-align: center;"><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/UM5ysNoLW7IINfCuiD9p.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="538" height="463" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">【审批事项】子界面</p>
<p>内容</p>
<ul>
<li>【抄送】包含抄送过来的申请信息列表；【归档】有所有员工申请通过并归档的信息列表；</li>
<li>【抄送记录】界面与【归档记录】页面。</li>
</ul>
<p>业务员</p>
<ul>
<li>【审批事项】中，业务员可以查看所有员工的审批申请信息，且所有信息按照【审批中】、【已审批】及【申请记录】分类；【申请记录可以查看所有审批事项的进程，包括“同意”“不同意”和“审核中”；</li>
<li>【审批中】和【已审批】可按照时间先后顺序、员工信息、报销类型等进行筛选查看，点击【详情】进入申请详情页进行审批；</li>
<li>【抄送记录】为业务员申请抄送给相应人员列表记录；</li>
<li>【归档记录】为所有人员申请归档记录。</li>
</ul>
<p>财务</p>
<p>【审批事项】、【抄送记录】与【归档记录】显示内容与业务员相同。</p>
<p><strong>操作流程</strong></p>
<p><strong>业务员审批界面：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/sASWZvP2A1Lbp5j6Bkd4.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="538" height="383" referrerpolicy="no-referrer"></p>
<p>内容</p>
<ul>
<li>审批中页面包含“审批信息列表”与管理信息列表功能；</li>
<li>审批详情页面包含申请的详细信息以及同意&驳回操作界面。</li>
</ul>
<p><strong>审批中页面与审批详情页面：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Ibm2T9ZJ3GNtHTr8gkh9.png" alt width="805" height="361" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">不同意提交页面、同意提交页面及抄送页面</p>
<p>内容：分别包含驳回对象、提交对象、抄送对象以及提交/抄送意见</p>
<p><strong>业务员抄送操作界面：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/gKifBZ4Zdggt2vuIe7YJ.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="808" height="456" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">从左到右分别为查看业务员环节不同意页面、业务员同意页面以及同意并抄送页面</p>
<p>内容：包含申请基础信息以及审批进度信息。</p>
<p>审批状态查看界面：</p>
<p>业务员进行审批信息查看，根据审批进度进入不同页面：对于审批中的申请，审核通过后跳转至【同意提交】，提交至下一级（财务），【不同意】即驳回给申请人，且可以进行信息抄送，【抄送】后退回至流程页面，流程页面记录抄送人。</p>
<p><strong>财务审批界面：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/3g9dYoq7IkhSs46SKxaW.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="538" height="512" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">审批中页面与审批详情页面</p>
<p style="text-align: center;"><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/gKifBZ4Zdggt2vuIe7YJ.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="533" height="301" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">财务审批操作界面</p>
<p style="text-align: center;">不同意提交页面、同意提交页面及抄送页面</p>
<p style="text-align: center;"><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="PRD:SaaS平台OA系统迭代需求文档" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/cEyisJYwkOAqCaqFNKBB.png" alt="PRD:SaaS平台OA系统迭代需求文档" width="541" height="430" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">从左到右分别为查看财务环节同意页面和财务不同意页面</p>
<p>内容包含申请基础信息以及审批进度信息以及抄送信息。</p>
<p>财务流程查看界面：</p>
<p>财务审批界面基本与业务员审批界面相同，不同之处在于进度流程推进至财务。</p>
<p>对业务员提交对审批进行抽查，并对所有同类型数据进行批量同意或批量驳回，批量同意之后可选择再次提交，提交人依照公司具体情况自行选择；驳回的申请直接驳回至申请人处；且审核通过的报销需进行归档，全员归档记录为业务员、财务、管理层可查看，普通员工可查看自己申请归档记录。</p>
<h3>2. Web端页面设计</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/f3hS26W6wvaQjQQreFkZ.png" alt width="537" height="405" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/I982VsWDXF1LRexkD8ay.png" alt width="536" height="402" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">通用主界面</p>
<p style="text-align: center;">网页主页及【审批】主页</p>
<p>进入主页的界面为消息界面，选择最上方导航栏中【审批】右边转化为审批相关列表。</p>
<p><strong>1）员工界面</strong></p>
<p><strong>① 员工首页、审批页面、申请页面及申请操作页面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/DMKfMrzgl13hyR3kSeXw.png" alt width="537" height="404" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/3SXXhuzNW83GGd9iN6EE.png" alt width="538" height="405" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/sJR2l3e66TDbXcgI3wPP.png" alt width="536" height="349" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/BUPFXCsnzF6PywDCeVFu.png" alt width="533" height="400" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">从上到下分别为web端主页面、员工【审批】主页面、【新增申请】页面及在【新增申请】中选择具体审批事项后的填报页面</p>
<p>内容</p>
<ul>
<li>【新增页面】界面中占比更多的为各种类型的审批功能；</li>
<li>【填报】页面为详细信息的填写与提交。</li>
</ul>
<p>员工申请流程</p>
<ol>
<li>选择【审批】，主页面出现所有申请信息；</li>
<li>选择【新建申请】，主页面出现所有申请类型（最近常用、日常、财务、人事等），选择财务申请，进入申请主页面；</li>
<li>申请编号自动生成，其余信息填写与APP信息填写规则相同，填写完毕选择【提交】或【存储为草稿】。</li>
</ol>
<p><strong>② 员工审批进度查看</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Eq6wtcYpEJvOXkjORLkD.png" alt width="537" height="405" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Yqq08TZv9tDhCAgBEXo4.png" alt width="537" height="406" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/o0uUMEARcGX7jgicsBsK.png" alt width="543" height="392" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/k0GVlK4P78h8klTJmblk.png" alt width="643" height="336" referrerpolicy="no-referrer"></p>
<p>页面显示从上到下分别为【审批列表】页面、【审批详情】页面，其余的为审批详情的各种状态显示。</p>
<p><strong>③ 抄送给我、档案记录与审批设置</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nyoyVY3ImhwLRGlVcNte.png" alt width="642" height="486" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hASiCr3Cnpfp6dZARjjV.png" alt width="645" height="485" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/E7xmOopsZkkPHRyDGhXk.png" alt width="643" height="483" referrerpolicy="no-referrer"></p>
<p>内容</p>
<ul>
<li>【审批列表】本人所有审批事项列表；</li>
<li>【审批详情】点击每条审批信息，页面右侧向左滑出具体审批进度；</li>
<li>【抄送给我】内容包括所有抄送过来的信息；</li>
<li>【档案记录】包括本人的所有申请归档的记录。</li>
</ul>
<p>员工查看信息页面</p>
<ul>
<li>【审批列表】：【审批列表】中，所有申请按照【审核中】、【不同意】和【同意】进行排列，可以通过“按照时间先后”“项目类型”等进行分类；点击具体信息，页面右侧弹出相应申请状态框，该信息仅供查看；</li>
<li>【抄送给我】：查看抄送消息；</li>
<li>【档案记录】：查看本人申请归档的历史记录；</li>
<li>【审批设置】：普通员工暂无权限修改审批设置。</li>
</ul>
<p><strong>④ 申请修改页面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/1mkcJ50TwwkeuKxN9lqS.png" alt width="640" height="484" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/XLOCGrIQqTKAqQKWNRel.png" alt width="649" height="487" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">员工申请修改界面及申请修改详情界面</p>
<p>内容</p>
<ul>
<li>申请修改界面包含所有被驳回的申请；</li>
<li>申请详情页包括具体申请填写信息，以及申请再次提交操作。</li>
</ul>
<p>对于未通过的申请，员工可直接在修改申请页面查看，点击相关申请进入修改页面，修改完毕后选择【再次提交】或【删除】。</p>
<p><strong>2）职能部门审批界面</strong></p>
<p><strong>① 业务员审批界面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xUpTwE5gYI2sWAeifKMf.png" alt width="642" height="484" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hnQTZhAouv9MhG7ws5S2.png" alt width="643" height="485" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/pE4sTMdSzwU0znU9zvNS.png" alt width="642" height="462" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/NUkNqmvnJxM8C1UnAMWR.png" alt width="642" height="460" referrerpolicy="no-referrer"></p>
<p>前两张页面分别为业务员审批界面、审批详情界面，右侧为审批结束至下一级、不同状态呈现页面及抄送操作界面。</p>
<p>内容</p>
<ul>
<li>审批界面包含公司所有员工申请事项；</li>
<li>审批详情有具体申请信息及相关物料展示，核对后对该申请进行下一步（同意与否以及抄送）操作。</li>
</ul>
<p>业务员</p>
<ol>
<li>【审批】业务员的【审批】信息为所有员工提交的信息，按照查看与否分为“新消息”及“历史信息”；</li>
<li>选择“审核中”的申请信息，页面右侧弹出申请详情，该页面供业务员操作；</li>
<li>同意申请将跳转至提交给下一级，驳回则直接驳回至申请人。信息提交之后即可抄送信息给相应人员。</li>
</ol>
<p><strong>② 财务审批界面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/UEjDyzZKl4PnOx2W7lms.png" alt width="648" height="490" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/aQYvt6zDBY7e7hhLbiRT.png" alt width="646" height="488" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ql6fun8P6cNt7iCjrR5D.png" alt width="645" height="462" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/sgI2DwNNnzX0u4Vufyb0.png" alt width="642" height="464" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">从左到右为财务审批界面和审批详情界面，界面内容与业务员相关界面相同</p>
<p>财务审批界面：</p>
<p>财务审批同理，驳回申请直接驳回至申请人。</p>
<p><strong>③ 业务员【抄送】、【归档】及【审批设置】界面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/KqnESR1axm0i8yX0ac3O.png" alt width="642" height="486" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/7oKwqssUWIxasY6ViCB2.png" alt width="647" height="489" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/kqAWcQlVMFZMWNnqOrlM.png" alt width="642" height="482" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">从上至下分别为【抄送给我】界面、【档案记录】界面及【审批设置】界面</p>
<p>内容</p>
<ul>
<li>【抄送给我】内容包括所有抄送过来的信息；</li>
<li>【档案记录】包括本人的所有申请归档的记录；</li>
<li>【审批设置】为对员工申请时，所提交的物料进行自定义。</li>
</ul>
<p>业务员查看页面</p>
<ul>
<li>业务员查看信息页面和普通员工相同，区别点在于档案记录业务员可查看所有员工申请的归档记录；</li>
<li>业务员无权限设置【审批设置】。</li>
</ul>
<p><strong>④ 财务【抄送】、【档案】及【审批设置】界面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Lt44vE7Qg9PXmIKz5EkL.png" alt width="641" height="480" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/q2QkNkuVJDD8fqiZ9pfg.png" alt width="642" height="482" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/aGyuKkOAfzuWIl9S9gac.png" alt width="644" height="484" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/seYqFgXPclCUrbVztZu4.png" alt width="642" height="483" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/DN7yz1BxZ05oeId9DrlM.png" alt width="644" height="569" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nE6laSBBKfFHokZvQz6m.png" alt width="645" height="489" referrerpolicy="no-referrer"></p>
<p>从上至下内容分别为【抄送给我】界面、【档案记录】界面、【审批设置】界面及【审批设置】详情页界面。</p>
<p>内容：</p>
<ul>
<li>【抄送给我】与【档案记录】界面内容与业务员相关界面相同；</li>
<li>【审批设置】界面主要为编辑审批表操作页面，除了程序设定的审批栏，财务可以根据自身需求增加或删除相应的事项。</li>
</ul>
<p>财务查看及自定义审批设置：</p>
<p>财务查看信息情况和业务员权限相同，不同之处在于财务有权限自定义审批设置，即由财务选择需要更改提交内容的申请事项，进入修改页面之后，参考现有的初始信息再对其他需要提交的材料进行自定义编辑。</p>
<p>提交的材料包括且不限于附件、日期、数字，且有【存储为草稿】、【预览】与【确认修改】功能。</p>
<h2 id="toc-6">六、总结</h2>
<p>此次版本迭代同时迭代APP端与web端，根据客户需求同步上线财务（发票）审批流程APP端优化了一线员工（不在办公区时）报销审批流程，使得报销速度提升，web端使得报销流程更加规范化，更有利于职能部门对相关审批信息的设置。</p>
<p> </p>
<p>本文由 @三只 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5041991" data-author="1270997" data-avatar="https://static.woshipm.com/APP_U_202107_20210726132650_9890.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            