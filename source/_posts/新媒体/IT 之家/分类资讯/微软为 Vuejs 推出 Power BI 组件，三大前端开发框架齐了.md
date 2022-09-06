
---
title: '微软为 Vue.js 推出 Power BI 组件，三大前端开发框架齐了'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/9/a6bec6d5-6444-47ce-8802-2f91edb687ad.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzE0OC5wbmc=,g_6,x_15,y_0,a_0,t_100'
author: IT 之家
comments: false
date: Tue, 06 Sep 2022 06:10:49 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/9/a6bec6d5-6444-47ce-8802-2f91edb687ad.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzE0OC5wbmc=,g_6,x_15,y_0,a_0,t_100'
---

<div>   
<p data-vmark="9a89"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 9 月 6 日消息，继 React 和 Angular 之后，微软今日宣布为另一大前端开发框架 <span class="accentTextColor">Vue.js</span> 推出了 Power BI 组件。</p><p style="text-align: center;" data-vmark="8c61"><img src="https://img.ithome.com/newsuploadfiles/2022/9/a6bec6d5-6444-47ce-8802-2f91edb687ad.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzE0OC5wbmc=,g_6,x_15,y_0,a_0,t_100" w="960" h="596" title="微软为 Vue.js 推出 Power BI 组件，三大前端开发框架齐了" width="960" height="509" referrerpolicy="no-referrer"></p><p data-vmark="c4ff">React、Angular  和 Vue.js 都是著名的 JavaScript 框架，<span class="accentTextColor">微软 Power BI 则是一款数据可视化工具</span>，可轻松地连接到数据、对数据进行建模和可视化，从而创建报表等。</p><p style="text-align: center;" data-vmark="b8ea"><img src="https://img.ithome.com/newsuploadfiles/2022/9/b02f8757-3890-4b4d-9665-1c5f7bfe9fac.png" w="925" h="331" title="微软为 Vue.js 推出 Power BI 组件，三大前端开发框架齐了" width="925" height="293" referrerpolicy="no-referrer"></p><p data-vmark="5e61">IT之家了解到，微软 Power BI 支持 Vue.js 后，开发者就可以使用该工具分析平台上的数据，并支持嵌入仪表板、问答和其他 Power BI 功能小组件。</p><p style="text-align: center;" data-vmark="5abe"><img src="https://img.ithome.com/newsuploadfiles/2022/9/00c4e221-1318-4988-bf67-6a59ba63ff65.gif" w="1440" h="695" title="微软为 Vue.js 推出 Power BI 组件，三大前端开发框架齐了" width="1440" height="396" referrerpolicy="no-referrer"></p><p style="text-align: justify;" data-vmark="39e5"><strong>导入库：</strong></p><pre class="brush:javascript;toolbar:false;">import &#123; PowerBIReportEmbed&#125; from 'powerbi-client-vue-js';</pre><p style="text-align: justify;" data-vmark="5d82"><strong>嵌入示例：</strong></p><pre><PowerBIReportEmbed
    :embedConfig = &#123;&#123;
        type: "report",
        id: "<Report Id>",
        embedUrl: "<Embed Url>",
        accessToken: "<Access Token>",
        tokenType: models.TokenType.Embed,
        settings: &#123;
            panes: &#123;
                filters: &#123;
                    expanded: false,
                    visible: false
                &#125;
            &#125;,
            background: models.BackgroundType.Transparent,
        &#125;
    &#125;&#125;

    :cssClassName = &#123; "reportClass" &#125;

    :phasedEmbedding = &#123; false &#125;

    :eventHandlers = &#123;
        new Map([
            ['loaded', () => console.log('Report loaded');],
            ['rendered', () => console.log('Report rendered');],
            ['error', (event) => console.log(event.detail);]
        ])
    &#125;
>
</PowerBIReportEmbed></pre>
          
</div>
            