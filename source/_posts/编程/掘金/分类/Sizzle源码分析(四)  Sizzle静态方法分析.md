
---
title: 'Sizzle源码分析(四)  Sizzle静态方法分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6384'
author: 掘金
comments: false
date: Sat, 29 May 2021 22:03:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=6384'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简介</h2>
<p>Sizzle 的静态方法起了辅助的作用，帮助完成一些对元素属性获取或者转义一些选择器，完成一些对元素节点的排序等等。我会对这些方法进行一个注释与讲解，等把所有的这些辅助方法讲完后，会对sizzle的是怎么样选择到元素的一个流程，还有架构做一个梳理。解读方法的顺序基本是按照代码的先后顺序来讲。如果有误，请大家纠正。</p>
<h2 data-id="heading-1">matches</h2>
<p>对已有元素进行筛选</p>
<pre><code class="copyable">/**
 * [matches] 对已有元素进行筛选
 * @param  &#123;[type]&#125; expr    
 * @param  &#123;[type]&#125; elements
 * @return Sizzle elements
 */
Sizzle.matches = function(expr, elements) &#123;
     //selector, context, results, seed,这个就是种子元素中来过滤查找元素，不用在上下文中重新来查找
     return Sizzle(expr, null, null, elements);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Sizzle.matchesSelector</h2>
<p>查看当前元素含有的是否包含这个选择器</p>
<pre><code class="copyable">/**
 * [matchesSelector ] 查看当前元素含有的是否包含这个选择
 * @param  &#123;[element]&#125; elem 
 * @param  &#123;[string]&#125; expr 
 * @return &#123;[boolean]&#125;    true or false
 */
Sizzle.matchesSelector = function(elem, expr) &#123;
        // 设置当前的上下文的兼容性
        setDocument(elem);
        /**
         * support.matchesSelector 是否支持
         * documentIsHTML 是不是html
         * !nonnativeSelectorCache[expr + " "]  查看是否在缓存中为false
         * rbuggyMatches 不存在或!rbuggyMatches.test(expr) matches不存在bug
         * rbuggyQSA不存在或 就是QSA不存在bug 
         */
        if (support.matchesSelector && documentIsHTML &&
                !nonnativeSelectorCache[expr + " "] &&
                (!rbuggyMatches || !rbuggyMatches.test(expr)) &&
                (!rbuggyQSA || !rbuggyQSA.test(expr))) &#123;

                try &#123;
                        // 看是否能匹配上
                        var ret = matches.call(elem, expr);
                        // 如果选择器与元素匹配上 或者不是文档片段或者还在当前或者还在当前上下文
                        // IE 9's matchesSelector returns false on disconnected nodes
                        if (ret || support.disconnectedMatch ||

                                // As well, disconnected nodes are said to be in a document
                                // fragment in IE 9
                                elem.document && elem.document.nodeType !== 11) &#123;
                                // 直接返回true
                                return ret;
                        &#125;
                &#125; catch (e) &#123;
                        // 如果不能支持选择器放入 nonnativeSelectorCache
                        nonnativeSelectorCache(expr, true);
                &#125;
        &#125;
        // 走入catch就会走这里，重新进行元素的一个匹配，如果找道返回true
        return Sizzle(expr, document, null, [elem]).length > 0;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Sizzle.contains</h2>
<p>来表示传入的节点是否为该节点的后代节点，返回true or false</p>
<pre><code class="copyable">/**
 * [contains]
 * @param  &#123;[element]&#125; context
 * @param  &#123;[element]&#125; elem   
 * @return &#123;[boolean]&#125;        
 */
Sizzle.contains = function(context, elem) &#123;

        // Set document vars if needed
        // Support: IE 11+, Edge 17 - 18+
        // IE/Edge sometimes throw a "Permission denied" error when strict-comparing
        // two documents; shallow comparisons work.
        // eslint-disable-next-line eqeqeq
        // 根据文档来设置上下问
        if ((context.ownerDocument || context) != document) &#123;
                setDocument(context);
        &#125;
        // 来表示传入的节点是否为该节点的后代节点，返回true or false
        return contains(context, elem);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">Sizzle.escape</h2>
<p>转义css选择器，首先把选择器转为字符串，然后用正则匹配需要转义的字符串，替换成unicode字符。这两个方法我已经在前置内容中已经讲过了。大家没看的可以从前几篇文章中找一下呢</p>
<pre><code class="copyable">Sizzle.escape = function(sel) &#123;
        return (sel + "").replace(rcssescape, fcssescape);
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Sizzle.error</h2>
<p>传参返回一个错误提示</p>
<pre><code class="copyable">
Sizzle.error = function(msg) &#123;
        throw new Error("Syntax error, unrecognized expression: " + msg);
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Sizzle.uniqueSort</h2>
<p>这个方法主要做的是给文档排序，上次节代码里面我已经讲到了怎么给文档排序了，不了的可以查看一下。还有一个做用就是删除重复的文档。我记得上节也讲到了sortOrder 这个方法了，如果a === b 相等时候 hasDuplicate 为true，说明文档有重复或者元素重复。</p>
<p>// Support: Chrome 14-35+
// Always assume duplicates if they aren't passed to the comparison function
加入没有传递这个参数就是一只重复着
support.detectDuplicates = !!hasDuplicate; 其实就是转了个boolean类型。这行代码在jquery的2921行。</p>
<p>// One-time assignments</p>
<p>// Sort stability 这个代码是对排序稳定性的一个测试, expando 是sizzle + 一个时间戳。
sortOrder = function( a, b ) &#123;
if ( a === b ) &#123;
hasDuplicate = true;
&#125;
return 0;
&#125;
// 就这块return 0 expando还是原来的顺序 hasDuplicate = true;
support.sortStable = expando.split( "" ).sort( sortOrder ).join( "" ) === expando;</p>
<pre><code class="copyable">/**
 * Document sorting and removing duplicates
 * @param &#123;ArrayLike&#125; results
 */
Sizzle.uniqueSort = function(results) &#123;
        var elem,
                duplicates = [],
                j = 0,
                i = 0;

        // Unless we *know* we can detect duplicates, assume their presence
        // Document的时候回执行sortOrder方法，如果支持hasCompare? hasDuplicate是true，否则是false
        hasDuplicate = !support.detectDuplicates;
        //sizzle1622222893304 就是false，&& results.slice(0) 把result 返回一个新数组浅拷贝
        sortInput = !support.sortStable && results.slice(0);
        然后对results进行排序
        results.sort(sortOrder);
        if (hasDuplicate) &#123;
                while ((elem = results[i++])) &#123;
                        if (elem === results[i]) &#123;
                                j = duplicates.push(i);
                        &#125;
                &#125;
                // j 等于duplicates.length 存储的就是数字，duplicates存储的是重复的数字的位置
                while (j--) &#123;
                        results.splice(duplicates[j], 1);
                &#125;
        &#125;

        // Clear input after sorting to release objects
        // See https://github.com/jquery/sizzle/pull/225
        sortInput = null;
        返回删剩下没有重复的元素
        return results;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">Sizzle.getText</h2>
<p>获取元素或者一组元素的文本内容</p>
<pre><code class="copyable">/**
 * Utility function for retrieving the text value of an array of DOM nodes
 * @param &#123;Array|Element&#125; elem
 */
 、、
getText = Sizzle.getText = function( elem ) &#123;
var node,
ret = "",
i = 0,
nodeType = elem.nodeType;
        // 如果不存在nodeType属性，说明是类数组
if ( !nodeType ) &#123;

// If no nodeType, this is expected to be an array
while ( ( node = elem[ i++ ] ) ) &#123;
                        // 递归拿到元素的内容
// Do not traverse comment nodes
ret += getText( node );
&#125;
                // 如果是元素或者document 或者 文档片段
&#125; else if ( nodeType === 1 || nodeType === 9 || nodeType === 11 ) &#123;

// Use textContent for elements
// innerText usage removed for consistency of new lines (jQuery #11153)
                // 返回元素中文本内容
if ( typeof elem.textContent === "string" ) &#123;
return elem.textContent;
&#125; else &#123;
                        否则遍历递归每个兄弟节点拿到文本
// Traverse its children
for ( elem = elem.firstChild; elem; elem = elem.nextSibling ) &#123;
ret += getText( elem );
&#125;
&#125;
                // 若果是CDATA节点或者文本节点 ，返回nodevalue
&#125; else if ( nodeType === 3 || nodeType === 4 ) &#123;
return elem.nodeValue;
&#125;

// Do not include comment or processing instruction nodes

return ret;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Sizzle.selectors</h2>
<p>这个方法主要是绑定了 cacheLength、createPseudo、match、attrHandle、find、preFilter、filter、pseudos这个几个方法。</p>
<p>cacheLength 这个属性的作用是 方法createCache 的中keys的长度，如果超过keys的长度超过了50，让第一个缓存出队。</p>
<p>createPseudo：markFunction 这个方法默认是接收一个fn参数，给fn添加一个[expando] = true的属性。并返回这个fn。</p>
<p>matchExpr这个属性这个在分析一之时，我分析过了所以的属性，用来匹配各种选择器。
attrHandle： 空对象 Expr.attrHandle[arr[i]] = handler;</p>
<p>find： 空对象,在setDocument初始化的的时候赋予的对应的key:value，返回元素数组 不明白看看上一章</p>
<p>relative： 选择的相对位置</p>
<p>preFilter： 预过滤器</p>
<p>filter：过滤器 在setDocument初始化的的时候赋予的对应的key:value，返回true or false</p>
<p>pseudos：伪类选择器</p>
<p>这块处理我会在下节继续接着解析css选择器，选中html元素结合着把这块来一个传插，并举一些实际的代码。
这块相对比较好理解，会举几个方法来讲一下。这块不理解可以先看，下章sizzle是怎么选择对这些选择器是如何处理的。</p>
<pre><code class="copyable"> Sizzle.selectors = &#123;
// Can be adjusted by the user
cacheLength: 50,
createPseudo: markFunction,
match: matchExpr,

attrHandle: &#123;&#125;,

find: &#123;&#125;,
        //我们匹配选择器dir 这样处理 relative['dir'] ,通过这样来拿到这元素位置
relative: &#123;
">": &#123; dir: "parentNode", first: true &#125;,
" ": &#123; dir: "parentNode" &#125;,
"+": &#123; dir: "previousSibling", first: true &#125;,
"~": &#123; dir: "previousSibling" &#125;
&#125;,
        // 这块的preFilter做的处理，预先解析,生成的token做一个预判，
preFilter: &#123;
"ATTR": function( match ) &#123;
match[ 1 ] = match[ 1 ].replace( runescape, funescape );

// Move the given value to match[3] whether quoted or unquoted
match[ 3 ] = ( match[ 3 ] || match[ 4 ] ||
match[ 5 ] || "" ).replace( runescape, funescape );

if ( match[ 2 ] === "~=" ) &#123;
match[ 3 ] = " " + match[ 3 ] + " ";
&#125;

return match.slice( 0, 4 );
&#125;,
                 /*
                  match:  [0: ":nth-child(2)"
                    1: "nth"
                    2: "child"
                    3: "2"
                    4: 0
                    5: 2
                    6: undefined
                    7: ""
                    8: "2"
                    groups: undefined
                    index: 0
                    input: ":nth-child(2)"
                    length: 9]
                 */
"CHILD": function( match ) &#123;
/* matches from matchExpr["CHILD"]
1 type (only|nth|...)
2 what (child|of-type)
3 argument (even|odd|\d*|\d*n([+-]\d+)?|...)
4 xn-component of xn+y argument ([+-]?\d*n|)
5 sign of xn-component
6 x of xn-component
7 sign of y-component
8 y of y-component
*/
                       // 拿到nth后代选择器
match[ 1 ] = match[ 1 ].toLowerCase();
                      //  如果是nth 
if ( match[ 1 ].slice( 0, 3 ) === "nth" ) &#123;
                                // 判断后端选择的nth-child(arg) arg是否有参数or 0
// nth-* requires argument
if ( !match[ 3 ] ) &#123;
Sizzle.error( match[ 0 ] );
&#125;
                                
// numeric x and y parameters for Expr.filter.CHILD
// remember that false/true cast respectively to 0/1
match[ 4 ] = +( match[ 4 ] ?
match[ 5 ] + ( match[ 6 ] || 1 ) :
2 * ( match[ 3 ] === "even" || match[ 3 ] === "odd" ) );
match[ 5 ] = +( ( match[ 7 ] + match[ 8 ] ) || match[ 3 ] === "odd" );
                                 其他选择器报错
// other types prohibit arguments
&#125; else if ( match[ 3 ] ) &#123;
Sizzle.error( match[ 0 ] );
&#125;
                         //返回组装后的租户在哪个结果
return match;
&#125;,

"PSEUDO": function( match ) &#123;
var excess,
unquoted = !match[ 6 ] && match[ 2 ];

if ( matchExpr[ "CHILD" ].test( match[ 0 ] ) ) &#123;
return null;
&#125;

// Accept quoted arguments as-is
if ( match[ 3 ] ) &#123;
match[ 2 ] = match[ 4 ] || match[ 5 ] || "";

// Strip excess characters from unquoted arguments
&#125; else if ( unquoted && rpseudo.test( unquoted ) &&

// Get excess from tokenize (recursively)
( excess = tokenize( unquoted, true ) ) &&

// advance to the next closing parenthesis
( excess = unquoted.indexOf( ")", unquoted.length - excess ) - unquoted.length ) ) &#123;

// excess is a negative index
match[ 0 ] = match[ 0 ].slice( 0, excess );
match[ 2 ] = unquoted.slice( 0, excess );
&#125;

// Return only captures needed by the pseudo filter method (type and argument)
return match.slice( 0, 3 );
&#125;
&#125;,

filter: &#123;

"TAG": function( nodeNameSelector ) &#123;
var nodeName = nodeNameSelector.replace( runescape, funescape ).toLowerCase();
return nodeNameSelector === "*" ?
function() &#123;
return true;
&#125; :
function( elem ) &#123;
return elem.nodeName && elem.nodeName.toLowerCase() === nodeName;
&#125;;
&#125;,

"CLASS": function( className ) &#123;
var pattern = classCache[ className + " " ];

return pattern ||
( pattern = new RegExp( "(^|" + whitespace +
")" + className + "(" + whitespace + "|$)" ) ) && classCache(
className, function( elem ) &#123;
return pattern.test(
typeof elem.className === "string" && elem.className ||
typeof elem.getAttribute !== "undefined" &&
elem.getAttribute( "class" ) ||
""
);
&#125; );
&#125;,

"ATTR": function( name, operator, check ) &#123;
return function( elem ) &#123;
var result = Sizzle.attr( elem, name );

if ( result == null ) &#123;
return operator === "!=";
&#125;
if ( !operator ) &#123;
return true;
&#125;

result += "";

/* eslint-disable max-len */

return operator === "=" ? result === check :
operator === "!=" ? result !== check :
operator === "^=" ? check && result.indexOf( check ) === 0 :
operator === "*=" ? check && result.indexOf( check ) > -1 :
operator === "$=" ? check && result.slice( -check.length ) === check :
operator === "~=" ? ( " " + result.replace( rwhitespace, " " ) + " " ).indexOf( check ) > -1 :
operator === "|=" ? result === check || result.slice( 0, check.length + 1 ) === check + "-" :
false;
/* eslint-enable max-len */

&#125;;
&#125;,

"CHILD": function( type, what, _argument, first, last ) &#123;
var simple = type.slice( 0, 3 ) !== "nth",
forward = type.slice( -4 ) !== "last",
ofType = what === "of-type";

return first === 1 && last === 0 ?

// Shortcut for :nth-*(n)
function( elem ) &#123;
return !!elem.parentNode;
&#125; :

function( elem, _context, xml ) &#123;
var cache, uniqueCache, outerCache, node, nodeIndex, start,
dir = simple !== forward ? "nextSibling" : "previousSibling",
parent = elem.parentNode,
name = ofType && elem.nodeName.toLowerCase(),
useCache = !xml && !ofType,
diff = false;

if ( parent ) &#123;

// :(first|last|only)-(child|of-type)
if ( simple ) &#123;
while ( dir ) &#123;
node = elem;
while ( ( node = node[ dir ] ) ) &#123;
if ( ofType ?
node.nodeName.toLowerCase() === name :
node.nodeType === 1 ) &#123;

return false;
&#125;
&#125;

// Reverse direction for :only-* (if we haven't yet done so)
start = dir = type === "only" && !start && "nextSibling";
&#125;
return true;
&#125;

start = [ forward ? parent.firstChild : parent.lastChild ];

// non-xml :nth-child(...) stores cache data on `parent`
if ( forward && useCache ) &#123;

// Seek `elem` from a previously-cached index

// ...in a gzip-friendly way
node = parent;
outerCache = node[ expando ] || ( node[ expando ] = &#123;&#125; );

// Support: IE <9 only
// Defend against cloned attroperties (jQuery gh-1709)
uniqueCache = outerCache[ node.uniqueID ] ||
( outerCache[ node.uniqueID ] = &#123;&#125; );

cache = uniqueCache[ type ] || [];
nodeIndex = cache[ 0 ] === dirruns && cache[ 1 ];
diff = nodeIndex && cache[ 2 ];
node = nodeIndex && parent.childNodes[ nodeIndex ];

while ( ( node = ++nodeIndex && node && node[ dir ] ||

// Fallback to seeking `elem` from the start
( diff = nodeIndex = 0 ) || start.pop() ) ) &#123;

// When found, cache indexes on `parent` and break
if ( node.nodeType === 1 && ++diff && node === elem ) &#123;
uniqueCache[ type ] = [ dirruns, nodeIndex, diff ];
break;
&#125;
&#125;

&#125; else &#123;

// Use previously-cached element index if available
if ( useCache ) &#123;

// ...in a gzip-friendly way
node = elem;
outerCache = node[ expando ] || ( node[ expando ] = &#123;&#125; );

// Support: IE <9 only
// Defend against cloned attroperties (jQuery gh-1709)
uniqueCache = outerCache[ node.uniqueID ] ||
( outerCache[ node.uniqueID ] = &#123;&#125; );

cache = uniqueCache[ type ] || [];
nodeIndex = cache[ 0 ] === dirruns && cache[ 1 ];
diff = nodeIndex;
&#125;

// xml :nth-child(...)
// or :nth-last-child(...) or :nth(-last)?-of-type(...)
if ( diff === false ) &#123;

// Use the same loop as above to seek `elem` from the start
while ( ( node = ++nodeIndex && node && node[ dir ] ||
( diff = nodeIndex = 0 ) || start.pop() ) ) &#123;

if ( ( ofType ?
node.nodeName.toLowerCase() === name :
node.nodeType === 1 ) &&
++diff ) &#123;

// Cache the index of each encountered element
if ( useCache ) &#123;
outerCache = node[ expando ] ||
( node[ expando ] = &#123;&#125; );

// Support: IE <9 only
// Defend against cloned attroperties (jQuery gh-1709)
uniqueCache = outerCache[ node.uniqueID ] ||
( outerCache[ node.uniqueID ] = &#123;&#125; );

uniqueCache[ type ] = [ dirruns, diff ];
&#125;

if ( node === elem ) &#123;
break;
&#125;
&#125;
&#125;
&#125;
&#125;

// Incorporate the offset, then check against cycle size
diff -= last;
return diff === first || ( diff % first === 0 && diff / first >= 0 );
&#125;
&#125;;
&#125;,

"PSEUDO": function( pseudo, argument ) &#123;

// pseudo-class names are case-insensitive
// http://www.w3.org/TR/selectors/#pseudo-classes
// Prioritize by case sensitivity in case custom pseudos are added with uppercase letters
// Remember that setFilters inherits from pseudos
var args,
fn = Expr.pseudos[ pseudo ] || Expr.setFilters[ pseudo.toLowerCase() ] ||
Sizzle.error( "unsupported pseudo: " + pseudo );

// The user may use createPseudo to indicate that
// arguments are needed to create the filter function
// just as Sizzle does
if ( fn[ expando ] ) &#123;
return fn( argument );
&#125;

// But maintain support for old signatures
if ( fn.length > 1 ) &#123;
args = [ pseudo, pseudo, "", argument ];
return Expr.setFilters.hasOwnProperty( pseudo.toLowerCase() ) ?
markFunction( function( seed, matches ) &#123;
var idx,
matched = fn( seed, argument ),
i = matched.length;
while ( i-- ) &#123;
idx = indexOf( seed, matched[ i ] );
seed[ idx ] = !( matches[ idx ] = matched[ i ] );
&#125;
&#125; ) :
function( elem ) &#123;
return fn( elem, 0, args );
&#125;;
&#125;

return fn;
&#125;
&#125;,

pseudos: &#123;

// Potentially complex pseudos
"not": markFunction( function( selector ) &#123;

// Trim the selector passed to compile
// to avoid treating leading and trailing
// spaces as combinators
var input = [],
results = [],
matcher = compile( selector.replace( rtrim, "$1" ) );

return matcher[ expando ] ?
markFunction( function( seed, matches, _context, xml ) &#123;
var elem,
unmatched = matcher( seed, null, xml, [] ),
i = seed.length;

// Match elements unmatched by `matcher`
while ( i-- ) &#123;
if ( ( elem = unmatched[ i ] ) ) &#123;
seed[ i ] = !( matches[ i ] = elem );
&#125;
&#125;
&#125; ) :
function( elem, _context, xml ) &#123;
input[ 0 ] = elem;
matcher( input, null, xml, results );

// Don't keep the element (issue #299)
input[ 0 ] = null;
return !results.pop();
&#125;;
&#125; ),

"has": markFunction( function( selector ) &#123;
return function( elem ) &#123;
return Sizzle( selector, elem ).length > 0;
&#125;;
&#125; ),

"contains": markFunction( function( text ) &#123;
text = text.replace( runescape, funescape );
return function( elem ) &#123;
return ( elem.textContent || getText( elem ) ).indexOf( text ) > -1;
&#125;;
&#125; ),

// "Whether an element is represented by a :lang() selector
// is based solely on the element's language value
// being equal to the identifier C,
// or beginning with the identifier C immediately followed by "-".
// The matching of C against the element's language value is performed case-insensitively.
// The identifier C does not have to be a valid language name."
// http://www.w3.org/TR/selectors/#lang-pseudo
"lang": markFunction( function( lang ) &#123;

// lang value must be a valid identifier
if ( !ridentifier.test( lang || "" ) ) &#123;
Sizzle.error( "unsupported lang: " + lang );
&#125;
lang = lang.replace( runescape, funescape ).toLowerCase();
return function( elem ) &#123;
var elemLang;
do &#123;
if ( ( elemLang = documentIsHTML ?
elem.lang :
elem.getAttribute( "xml:lang" ) || elem.getAttribute( "lang" ) ) ) &#123;

elemLang = elemLang.toLowerCase();
return elemLang === lang || elemLang.indexOf( lang + "-" ) === 0;
&#125;
&#125; while ( ( elem = elem.parentNode ) && elem.nodeType === 1 );
return false;
&#125;;
&#125; ),

// Miscellaneous
"target": function( elem ) &#123;
var hash = window.location && window.location.hash;
return hash && hash.slice( 1 ) === elem.id;
&#125;,

"root": function( elem ) &#123;
return elem === docElem;
&#125;,

"focus": function( elem ) &#123;
return elem === document.activeElement &&
( !document.hasFocus || document.hasFocus() ) &&
!!( elem.type || elem.href || ~elem.tabIndex );
&#125;,

// Boolean properties
"enabled": createDisabledPseudo( false ),
"disabled": createDisabledPseudo( true ),

"checked": function( elem ) &#123;

// In CSS3, :checked should return both checked and selected elements
// http://www.w3.org/TR/2011/REC-css3-selectors-20110929/#checked
var nodeName = elem.nodeName.toLowerCase();
return ( nodeName === "input" && !!elem.checked ) ||
( nodeName === "option" && !!elem.selected );
&#125;,

"selected": function( elem ) &#123;

// Accessing this property makes selected-by-default
// options in Safari work properly
if ( elem.parentNode ) &#123;
// eslint-disable-next-line no-unused-expressions
elem.parentNode.selectedIndex;
&#125;

return elem.selected === true;
&#125;,

// Contents
"empty": function( elem ) &#123;

// http://www.w3.org/TR/selectors/#empty-pseudo
// :empty is negated by element (1) or content nodes (text: 3; cdata: 4; entity ref: 5),
//   but not by others (comment: 8; processing instruction: 7; etc.)
// nodeType < 6 works because attributes (2) do not appear as children
for ( elem = elem.firstChild; elem; elem = elem.nextSibling ) &#123;
if ( elem.nodeType < 6 ) &#123;
return false;
&#125;
&#125;
return true;
&#125;,

"parent": function( elem ) &#123;
return !Expr.pseudos[ "empty" ]( elem );
&#125;,

// Element/input types
"header": function( elem ) &#123;
return rheader.test( elem.nodeName );
&#125;,

"input": function( elem ) &#123;
return rinputs.test( elem.nodeName );
&#125;,

"button": function( elem ) &#123;
var name = elem.nodeName.toLowerCase();
return name === "input" && elem.type === "button" || name === "button";
&#125;,

"text": function( elem ) &#123;
var attr;
return elem.nodeName.toLowerCase() === "input" &&
elem.type === "text" &&

// Support: IE<8
// New HTML5 attribute values (e.g., "search") appear with elem.type === "text"
( ( attr = elem.getAttribute( "type" ) ) == null ||
attr.toLowerCase() === "text" );
&#125;,

// Position-in-collection
"first": createPositionalPseudo( function() &#123;
return [ 0 ];
&#125; ),

"last": createPositionalPseudo( function( _matchIndexes, length ) &#123;
return [ length - 1 ];
&#125; ),

"eq": createPositionalPseudo( function( _matchIndexes, length, argument ) &#123;
return [ argument < 0 ? argument + length : argument ];
&#125; ),

"even": createPositionalPseudo( function( matchIndexes, length ) &#123;
var i = 0;
for ( ; i < length; i += 2 ) &#123;
matchIndexes.push( i );
&#125;
return matchIndexes;
&#125; ),

"odd": createPositionalPseudo( function( matchIndexes, length ) &#123;
var i = 1;
for ( ; i < length; i += 2 ) &#123;
matchIndexes.push( i );
&#125;
return matchIndexes;
&#125; ),

"lt": createPositionalPseudo( function( matchIndexes, length, argument ) &#123;
var i = argument < 0 ?
argument + length :
argument > length ?
length :
argument;
for ( ; --i >= 0; ) &#123;
matchIndexes.push( i );
&#125;
return matchIndexes;
&#125; ),

"gt": createPositionalPseudo( function( matchIndexes, length, argument ) &#123;
var i = argument < 0 ? argument + length : argument;
for ( ; ++i < length; ) &#123;
matchIndexes.push( i );
&#125;
return matchIndexes;
&#125; )
&#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://juejin.cn/editor/drafts/6932287283819184142" target="_blank">Sizzle源码分析(一) 基本概念</a></p>
<p><a href="https://juejin.cn/editor/drafts/6954012064121618463" target="_blank">Sizzle源码分析(二) 工具方法</a></p>
<p><a href="https://juejin.cn/post/6966980155960983589/" target="_blank">Sizzle源码分析(三) 兼容处理</a></p>
<p><a href="https://juejin.cn/post/6967959340795822117/" target="_blank">Sizzle源码分析(四) sizzle静态方法分析</a>
<a href="https://juejin.cn/post/6967959340795822117/" target="_blank">Sizzle源码分析(四) sizzle静态方法分析</a></p></div>  
</div>
            