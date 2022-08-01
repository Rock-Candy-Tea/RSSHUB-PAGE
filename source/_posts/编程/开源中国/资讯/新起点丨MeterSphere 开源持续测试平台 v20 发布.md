
---
title: '新起点丨MeterSphere 开源持续测试平台 v2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/4aabff5dbe3445bd9085cffc69348c2d~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=Md69MWmr704N43yQId6TCRRq2hM%3D'
author: 开源中国
comments: false
date: Mon, 01 Aug 2022 11:33:00 GMT
thumbnail: 'https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/4aabff5dbe3445bd9085cffc69348c2d~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=Md69MWmr704N43yQId6TCRRq2hM%3D'
---

<div>   
<div class="content">
                                                                                            <p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>2022年8月1日，MeterSphere一站式开源持续测试平台正式发布v2.0版本。在经历了近三个月的v1.20 LTS版本迭代后，MeterSphere的系统稳定性与可用性得到进一步提升，在8月正式迎来全新的v2.0版本。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>在这一版本中，<strong><span style="color:#783887">MeterSphere导航栏菜单全新升级为经典的左右结构</span></strong>，支持菜单栏固定模式与图标简约的模式，在不改变用户操作习惯的基础上增加了界面右侧的可操作空间。在“测试跟踪”模块中，<strong><span style="color:#783887">测试计划支持关联UI测试用例执行</span></strong>，附件功能支持上传视频文件，测试用例支持批量关联需求；在“接口测试”模块，<strong><span style="color:#783887">在测试计划中运行的接口测试支持失败重试、自定义重试次数</span></strong>，以提升测试计划的成功率；<strong><span style="color:#783887">“UI测试”模块的页面元素支持使用Excel进行导入导出，UI场景用例支持批量执行</span></strong>；“工作台”模块支持一键同步接口变更；通用功能中，高级搜索支持自定义字段查询。</span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">新增功能</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><strong><span style="color:#783887">■ 导航栏全新升级</span></strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>MeterSphere v2.0版本将导航栏升级为混合导航布局，即垂直导航和水平导航。垂直导航显示一级菜单，支持菜单栏固定模式与图标简约模式，水平导航显示二级菜单，沉浸感高，同时扩大了页面的整体操作空间。</span></p> 
<div style="margin-left:0; margin-right:0; text-align:justify"> 
 <p><img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/4aabff5dbe3445bd9085cffc69348c2d~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=Md69MWmr704N43yQId6TCRRq2hM%3D" referrerpolicy="no-referrer"></p> 
 <p><span>图标简约模式，即垂直导航的收缩态。用户在某一具体测试分类下工作时，仅需要操作水平导航菜单即可完成当前测试分类下的工作闭环，从而减少干扰 ，增强沉浸体验。</span></p> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/40ad37cdec0a4bee901e9767f761f510~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=aUDGqkNdtm57%2FXzcwx10%2B%2BcOUkk%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <strong><span style="color:#783887">■ 测试计划支持关联UI测试用例执行（X-Pack增强包内）</span></strong>
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>MeterSphere自v1.20 LTS版本发布UI测试模块后，完成了一站式持续测试平台的雏形。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>在MeterSphere v2.0版本中，测试计划支持关联UI测试用例，实现了一个测试计划覆盖全部测试类型的需求。与接口测试一样，UI测试用例支持串行/并行执行，借助Grid的强大扩展能力，UI测试也支持多节点分布式运行。同时，测试计划已全面融入DevOps流水线，助力企业实现高质量的软件交付。</span></p> 
<div style="margin-left:0; margin-right:0; text-align:justify"> 
 <p><img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/3f464c94906744b58b6255ea03d814ae~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=BC5zMeMrzel47MWAe8aUDs6qHlY%3D" referrerpolicy="no-referrer"></p> 
 <p><span><strong><span style="color:#783887">■ 测试计划中运行的接口测试支持失败重试（X-Pack增强包内）</span></strong></span></p> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>MeterSphere v2.0版本在测试计划的运行配置中，针对接口测试（含单接口用例以及接口场景）增加了失败重试机制。接口请求执行失败后，会根据设定的重试次数再次发起请求，请求结果展示为最后一次的运行结果。测试报告会完整记录接口首次运行，以及最后10次运行的响应结果，供用户进行对比分析。</span></p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/c3ca0ece336f4b13a11a9f389e8a672e~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=i9l3cgXLLKkbHw5XPOhNDRZnBNY%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify"> 
 <p><img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/8ba006a868ed4c67b16506910989efad~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=kxiVJM0qtpXW%2Ft%2FRVnxcnrsBSXE%3D" referrerpolicy="no-referrer"></p> 
 <p><span><strong><span style="color:#783887">■ UI测试场景支持批量执行（X-Pack增强包内）</span></strong></span></p> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>MeterSphere v2.0版本中，为了提高UI测试用例的执行效率，新增了批量执行的功能。UI测试用例“批量运行”模式可以选择串行或并行模式，测试报告可以选择生成独立报告或集合报告。在测试报告中会按照场景、步骤、指令（同接口的请求级别）三个维度统计执行结果。</span></p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/902f74f973ec4b5484ce680c8e301a6f~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=VsWr3NFdbWuEKatAm2hkXGwXxlE%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify"> 
 <p><img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/39ec921e905541f481cfc4ac82442a9c~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=nH6fbhGnpZH6fx0V1U4qIYd9P6s%3D" referrerpolicy="no-referrer"></p> 
 <p><span><strong><span style="color:#783887">■ “工作台”模块支持一键同步接口变更（X-Pack增强包内）</span></strong></span></p> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>MeterSphere v2.0版本将“我的工作台”更名为“工作台”。新版本的“工作台”重点解决了API发生变更后自动更新接口用例的问题。当API发生变更后，系统根据用户自定义的数据流入规则将符合条件的接口用例展示在待更新列表中，用户可以逐条同步也可以批量同步API的指定信息或全部信息，将其更新至接口用例中。</span></p> 
<div style="margin-left:0; margin-right:0; text-align:justify"> 
 <p><img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/905e3296615b454581a142e1ee56e8c2~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=d4IoHpiWKxK9lqHutwzBaZz%2BN98%3D" referrerpolicy="no-referrer"></p> 
 <p><span>自定义“我的待办”→“接口用例”→“待更新列表”的数据流入规则。</span></p> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify"> 
 <p><img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/cae9fdef558d434a90e1b7f105df2634~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=8JDeykrNPS0Ohri66wMKtQMCMjM%3D" referrerpolicy="no-referrer"></p> 
 <p><span><strong><span style="color:#783887">■ 高级搜索支持自定义字段搜索</span></strong></span></p> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>MeterSphere v2.0版本对基础查询功能的“高级搜索”能力进行了增强。MeterSphere“测试跟踪”模块的功能用例模板、缺陷模板均支持添加自定义字段，v2.0版本中高级搜索功能支持添加自定义字段搜索。</span></p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/d29d133694a04d88abb2ccfa6dcbff44~noop.image?_iz=58558&from=article.pc_detail&x-expires=1659928436&x-signature=g2LC5GPTk5nMsDrnDg0QwwjTzvE%3D" referrerpolicy="no-referrer">
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">功能优化</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>测试跟踪：附件功能支持上传视频文件；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>测试跟踪：功能用例支持批量关联需求；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>测试跟踪：测试计划、测试评审关联用例支持按关联需求筛选用例；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>测试跟踪：测试计划报告增加运行环境展示；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>测试跟踪（X-Pack）：测试计划报告支持接口失败用例一键重跑；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>接口测试：首页数据统计优化；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>接口测试：API导入逻辑重构；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>接口测试：测试报告增加运行环境展示；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>接口测试：支持添加场景级别断言；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>接口测试（X-Pack）：集合报告支持失败用例一键重跑；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>UI测试（X-Pack）：页面元素支持Excel导入/导出管理；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>UI测试（X-Pack）：UI场景变量优化；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>UI测试（X-Pack）：高级设置中断言和数据提取功能展示优化；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#783887">■</span><span> </span>项目设置（X-Pack）：消息通知支持对接自定义WebHook。</span></p> 
<p style="color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><span>除了上述提到的新增功能和优化外，MeterSphere v2.0版本还包含很多其他功能的更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</span></p>
                                        </div>
                                      
</div>
            