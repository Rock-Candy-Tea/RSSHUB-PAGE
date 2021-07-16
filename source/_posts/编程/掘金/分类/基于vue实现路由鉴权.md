
---
title: '基于vue实现路由鉴权'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3901'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 22:28:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=3901'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>步骤1：登录后后端接口返回 如下结构数据：</p>
<pre><code class="copyable">&#123;
"data":[
&#123;"funcId":2,"funcName":"应用管理","parentId":1,"path":"/appBusinessManage","iconUrl":"d","sortId":1,"funcLevel":2,"children":[&#123;"funcId":7,"funcName":"应用管理","parentId":2,"path":"/appBusinessManage/index","iconUrl":"a","sortId":1,"funcLevel":3,"children":null&#125;]&#125;,
&#123;"funcId":3,"funcName":"角色管理","parentId":1,"path":"/roleManagement","iconUrl":"f","sortId":2,"funcLevel":2,"children":[&#123;"funcId":9,"funcName":"功能角色","parentId":3,"path":"/roleManagement/index","iconUrl":"a","sortId":1,"funcLevel":3,"children":null&#125;]&#125;,
&#123;"funcId":11,"funcName":"用户管理","parentId":1,"path":"/userManage","iconUrl":"a","sortId":3,"funcLevel":2,"children":[&#123;"funcId":26,"funcName":"用户管理","parentId":11,"path":"/admin/listUser","iconUrl":null,"sortId":11,"funcLevel":3,"children":null&#125;]&#125;,
&#123;"funcId":24,"funcName":"科室管理","parentId":1,"path":"/departmentManage","iconUrl":null,"sortId":4,"funcLevel":2,"children":[&#123;"funcId":25,"funcName":"科室管理","parentId":24,"path":"/departmentManage/index","iconUrl":null,"sortId":1,"funcLevel":3,"children":null&#125;]&#125;
],
"retCode":0
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>步骤2：将返回路由保存在store中 进行如下操作</p>
<pre><code class="copyable">saveAsyncRoutes(filterRoutes) &#123;
  const routes = getAsyncRoute(filterRoutes);
  router.addRoutes(routes);
  setStorage("asyncRoutes", filterRoutes);      
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>步骤3：路由文件前端写死内容</p>
<pre><code class="copyable">import Layout from "@/components/Layout";

const routerMap = [
    &#123;
        path: "/dashboardManage",
        component: Layout,
        redirect: "/dashboard/index",
        meta: &#123;
            title: "首页",
            icon: "desktop",
            name: "/dashboardManage"
        &#125;,
        children: [
            &#123;
                path: "/dashboard/index",
                component: () => import("@/views/dashboard/index.vue"),
                meta: &#123;
                    title: "首页",
                    name: "/dashboard/index",
                    hidden: true
                &#125;
            &#125;
        ]
    &#125;,
    &#123;
        path: "/appBusinessManage",
        component: Layout,
        meta: &#123;
            title: "应用管理",
            icon: "appstore",
            name: "/appBusinessManage"
        &#125;,
        redirect: "/appBusinessManage/index",
        children: [
            &#123;
                path: "/appBusinessManage/index",
                component: () => import("@/views/appBusinessManage"),
                meta: &#123;
                    title: "应用管理",
                    name: "/appBusinessManage/index"
                &#125;
            &#125;,
        ]
    &#125;,
    &#123;
        path: "/roleManagement",
        component: Layout,
        meta: &#123;
            title: "角色管理",
            icon: "contacts",
            name: "/roleManagement"
        &#125;,
        redirect: "/roleManagement/index",
        children: [
            &#123;
                path: "/roleManagement/index",
                component: () => import("@/views/roleManagement"),
                meta: &#123;
                    title: "功能角色",
                    name: "/roleManagement/index"
                &#125;
            &#125;,
            &#123;
                path: "/roleApplication/index",
                component: () => import("@/views/roleApplication"),
                meta: &#123;
                    title: "应用角色",
                    name: "/roleApplication/index"
                &#125;
            &#125;
        ]
    &#125;,

 
 
]
export default routerMap;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>步骤4:数据处理，getAsyncRoute 在下面文件中进行处理，ValidationRole为一个配置开关，如果返回true，代表启动动态路由，如果返回false，直接走前端写死路由即可</p>
<pre><code class="copyable">import routerMaps from '@/router/router.map';
import router2Map from '@/router/appRouter.ts';
import &#123; ValidationRole &#125; from '@/config';
import &#123; MenuStore &#125; from '../store/menu';
/**
 * @param roleRoutes 权限路由集合
 * @param routerMap   待挂载的路由集合
 * @param children   树节点
 * @param key   唯一key
 * @returns 通过权限过滤后的路由
 */
// 系统管理路由
export function getAsyncRoute(roleRoutes, routerMap = routerMaps, children = 'children', key = 'path') &#123;
    // 不需要权限验证时  直接返回完整路由
    if (!ValidationRole) &#123;
        return routerMaps;
    &#125;
    // 传来的权限路由不存在 则返回空[]
    if (!roleRoutes) &#123;
        return [];
    &#125;
    try &#123;
        roleRoutes = JSON.parse(roleRoutes);
    &#125; catch (error) &#123; &#125;
    //  对数组进行降维打击，将子路由children和父路由都放到一个维度的数组里面
    const afterSqueeze = squeeze(roleRoutes, children);
    console.log("afterSqueeze",afterSqueeze)
    // 所有权限路由path集合
    const pathList = afterSqueeze.map(r => r[key]);
    console.log("pathList",pathList)
    // 过滤权限路由
    console.log("routerMap",routerMap)
    const asyncRoute = filterRouter(routerMap, key);
    console.log("asyncRoute",asyncRoute)
    // 递归排序
    sortRoute(asyncRoute)
    return asyncRoute;


    /**
     * @default key =>'path'
     * @param key 服务端传来的路由的路径 通过此字段进行过滤
     * @param routes 待挂载的路由集合
     * @returns 过滤后的路由集合
     */
     前端写死的路由 根据 pathList 服务端返回的路由进行过滤，最终得到即将渲染的路由。  
    function filterRouter(routes, key = 'path') &#123;
        return routes.filter(r => &#123;
            if (pathList.includes(r.path)) &#123;
                const meta = afterSqueeze.find((j) => j[key] === r.path);
                r.meta = &#123; ...r.meta, ...meta &#125;;
                r.children && (r.children = filterRouter(r.children));
                return true;
            &#125;
        &#125;);
    &#125;
    /**
     *
     * @param routes 待排序的路由集合
     * 根据meta.sortOrder由小到大排序
     */
    function sortRoute(routes) &#123;
        routes.sort((a, b) => &#123;
            // tslint:disable: no-unused-expression
            a.children && sortRoute(a.children);
            b.children && sortRoute(b.children);
            // return a.meta.sortOrder - b.meta.sortOrder
            return 1;
        &#125;);
    &#125;

&#125;
/**
 * 数组降维
 * @param arr 待降维的数组
 * @param key 需要降维的字段
 * @returns  降维后的一维数组
 */
export function squeeze(arr, key = 'children') &#123;
    const newArr = [];

    function fn(v) &#123;
        v.map(r => &#123;
            newArr.push(r);
            if (r[key]) &#123;
                fn(r[key]);
            &#125;
        &#125;);
    &#125;
    fn(arr);
    return newArr;
&#125;
//# sourceMappingURL=permission.js.map
<span class="copy-code-btn">复制代码</span></code></pre>
<p>步骤5：渲染导航</p>
<pre><code class="copyable"> menuItem(r) &#123;
        let key = "";
        if (r.children && r.children.length > 0) &#123;
            key = r.children[0].path;
        &#125;
        else &#123;
            key = r.path;
        &#125;
        return (<a-menu-item key=&#123;key&#125;>
            &#123;r.meta.icon && (<a-icon type=&#123;r.meta.icon&#125; style="font-size:16px" />)&#125;
            <span class="padding-left">&#123;r.meta.title&#125;</span>
        </a-menu-item>);
    &#125;
    subItem(r) &#123;
        return (<a-sub-menu key=&#123;r.path&#125; onTitleClick=&#123;this.titleClick&#125; title=&#123;[
            <a-icon type=&#123;r.meta.icon&#125; style="font-size:16px" />,
            <span class="padding-left" v-text=&#123;r.meta.title&#125; />
        ]&#125;>
            &#123;r.children.map(i => this.menuItem(i))&#125;
        </a-sub-menu>);
    &#125;
    render() &#123;
        return (
        <a-layout-sider collapsible trigger=&#123;null&#125; v-model=&#123;this.$props.collapsed&#125; width=&#123;256&#125;>
                <a-menu onClick=&#123;this.menuClick&#125; selectedKeys=
                &#123;[this.$route.path]&#125; openKeys=&#123;this.openkeys&#125; mode="inline" 
                theme="light" style="height: 100%; ">
                <a-menu-item key="/dashboard/index">
                    <a-icon type="desktop" style="font-size:16px" />
                    <span class="padding-left">首页</span>
                </a-menu-item>
                    &#123;this.routerMaps.map((r) => r.children.length > 1
                        ? this.subItem(r)
                        : this.menuItem(r))
                     &#125;
                </a-menu> 
        </a-layout-sider>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            