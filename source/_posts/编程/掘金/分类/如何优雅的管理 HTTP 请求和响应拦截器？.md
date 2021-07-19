
---
title: '如何优雅的管理 HTTP 请求和响应拦截器？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ce1a9b0a66249048f323ed9b4b89478~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:18:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ce1a9b0a66249048f323ed9b4b89478~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:18px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:40px;margin-bottom:20px;color:#007fff;display:flex;align-items:center&#125;.markdown-body h1:hover:before,.markdown-body h2:hover:before,.markdown-body h3:hover:before,.markdown-body h4:hover:before,.markdown-body h5:hover:before,.markdown-body h6:hover:before&#123;transition:All .4s ease-in-out;transform:rotate(1turn)&#125;.markdown-body h1&#123;font-size:30px;background:linear-gradient(#fff 60%,#c6e3ff 0)&#125;.markdown-body h1:before&#123;content:"";display:inline-block;width:32px;height:32px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h2&#123;font-size:24px;background:linear-gradient(#fff 60%,#cce3fb 0)&#125;.markdown-body h2:before&#123;content:"";display:inline-block;width:24px;height:24px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3:before&#123;content:"";display:inline-block;width:18px;height:18px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h4&#123;font-size:18px&#125;.markdown-body h4:before&#123;content:"";display:inline-block;width:16px;height:16px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h5:before&#123;content:"";display:inline-block;width:15px;height:15px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h6&#123;font-size:14px&#125;.markdown-body h6:before&#123;content:"";display:inline-block;width:12px;height:12px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;border-bottom:2px solid #007fff;color:#007fff;padding-right:10px&#125;.markdown-body p&#123;letter-spacing:1px;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:10px auto&#125;.markdown-body hr&#123;border:none;border-top:1px dashed #92c8ff&#125;.markdown-body hr:before&#123;content:"✂";display:inline-block;position:relative;top:-12px;left:40px;padding:0 3px;color:#007fff;font-size:18px&#125;.markdown-body hr:after&#123;content:"按虚线剪开";position:relative;top:-15px;left:84%;padding:0 3px;color:#007fff;font-size:12px&#125;.markdown-body del&#123;color:#f44&#125;.markdown-body em&#123;color:#007fff;margin:0 2px&#125;.markdown-body strong&#123;color:#007fff;font-weight:bolder&#125;.markdown-body code&#123;word-break:break-word;border-radius:4px;overflow-x:auto;background-color:#e6f3ff;color:#007fff;font-weight:600;font-size:16px;padding:.065em .4em;border:1px solid #007fff&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:5px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:18px;font-weight:400;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8;border:none&#125;.markdown-body a&#123;text-decoration:none;color:#007fff;border-bottom:1px solid #007fff&#125;.markdown-body a:before&#123;content:"¶";margin-right:5px;font-size:22px&#125;.markdown-body a:after&#123;content:"↷";margin-left:2px;font-size:22px;display:none&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c;border-bottom:1px solid #275b8c&#125;.markdown-body a:active:after,.markdown-body a:hover:after&#123;display:inline-block&#125;.markdown-body table&#123;display:inline-block!important;font-size:16px;width:auto;max-width:100%;overflow:auto;border:1px solid #a5d3ff&#125;.markdown-body thead&#123;background:#c6e3ff;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#eef7ff&#125;.markdown-body tbody>tr:nth-child(odd)&#123;background-color:#f8fcff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #007fff;background-color:#eef7ff&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#007fff&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" title="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
</blockquote>
<blockquote>
<p>本文思路来自实际项目的重构总结，欢迎纠正和交流。如果对你有帮助，还请点赞👍收藏支持一下啦。</p>
</blockquote>
<p>最近重构一个老项目，发现其中处理请求的拦截器写得相当乱，于是我将整个项目的请求处理层重构了，目前已经在项目中正常运行。</p>
<p>本文会和大家分享我的重构思路和后续优化的思考，为方便与大家分享，我用 Vue3 实现一个简单 demo，思路是一致的，有兴趣的朋友可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpingan8787%2FLeo-JavaScript%2Fblob%2Fmaster%2FCute-Summary%2Fuseful-request-demo%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pingan8787/Leo-JavaScript/blob/master/Cute-Summary/useful-request-demo/index.html" ref="nofollow noopener noreferrer">在我 Github 查看</a>，本文会以这个 Vue 实现的 demo 为例介绍。</p>
<p>本文我会主要和大家分享以下几点：</p>
<ol>
<li>问题分析和方案设计；</li>
<li>重构后效果；</li>
<li>开发过程；</li>
<li>后期优化点；</li>
</ol>
<p>如果你还不清楚什么是 HTTP 请求和响应拦截器，那么可以先看看<a href="https://juejin.cn/post/6885471967714115597" target="_blank" title="https://juejin.cn/post/6885471967714115597">《77.9K Star 的 Axios 项目有哪些值得借鉴的地方》</a> 。</p>
<h2 data-id="heading-0">一、需求思考和方案设计</h2>
<h3 data-id="heading-1">1. 问题分析</h3>
<p>目前旧项目经过多位同事参与开发，拦截器存在以下问题：</p>
<ul>
<li>代码比较混乱，可读性差；</li>
<li>每个拦截器职责混乱，存在相互依赖；</li>
<li>逻辑上存在问题；</li>
<li>团队内部不同项目无法复用；</li>
</ul>
<h3 data-id="heading-2">2. 方案设计</h3>
<p>分析上面问题后，我初步的方案如下：
参考<strong>插件化架构设计</strong>，<strong>独立每个拦截器</strong>，将每个拦截器抽离成单独文件维护，做到<strong>职责单一</strong>，然后通过<strong>拦截器调度器</strong>进行调度和注册。</p>
<p>其拦截器调度过程如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ce1a9b0a66249048f323ed9b4b89478~tplv-k3u1fbpfcp-zoom-1.image" alt="拦截器调度过程" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">二、重构后效果</h2>
<p>代码其实比较简单，这里先看下最后实现效果：</p>
<h3 data-id="heading-4">1. 目录分层更加清晰</h3>
<p>重构后请求处理层的目录分层更加清晰，大致如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93071e340443455baa6465c74b738cdc~tplv-k3u1fbpfcp-zoom-1.image" alt="目录分层" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">2. 拦截器开发更加方便</h3>
<p>在后续业务拓展新的拦截器，仅需 3 个步骤既可以完成拦截器的开发和使用，拦截器调度器会<strong>自动调用所有拦截器</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/300d5d2b343f47d9822f38308b501ba3~tplv-k3u1fbpfcp-zoom-1.image" alt="拦截器开发更加方便" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">3. 每个拦截器职责更加单一，可插拔</h3>
<p>将每个拦截器抽成一个文件去实现，让每个拦截器<strong>职责分离且单一</strong>，当不需要使用某个拦截器时，随时可以替换，灵活插拔。</p>
<h2 data-id="heading-7">三、开发过程</h2>
<p>这里以我单独抽出来的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpingan8787%2FLeo-JavaScript%2Fblob%2Fmaster%2FCute-Summary%2Fuseful-request-demo%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pingan8787/Leo-JavaScript/blob/master/Cute-Summary/useful-request-demo/index.html" ref="nofollow noopener noreferrer">这个 demo 项目</a>为例来介绍。</p>
<h3 data-id="heading-8">1. 初始化目录结构</h3>
<p>按照前面设计的方案，首先需要在项目中创建一下目录结构：</p>
<pre><code class="hljs language-bash copyable" lang="bash">- request
- index.js      // 拦截器调度器
  - interceptors  
    - request     // 用来存放每个请求拦截器
    - index.js  // 管理所有请求拦截器，并做排序
    - response    // 用来存放每个响应拦截器
    - index.js  // 管理所有响应拦截器，并做排序
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2. 定义拦截器调度器</h3>
<p>因为项目采用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faxios%2Faxios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/axios/axios" ref="nofollow noopener noreferrer">axios 请求库</a>，所以我们需要先知道 axios 拦截器的使用方法，这里简单看下 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faxios%2Faxios%23interceptors" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/axios/axios#interceptors" ref="nofollow noopener noreferrer">axios 文档上如何使用拦截器</a>的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 添加请求拦截器</span>
axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) </span>&#123;
    <span class="hljs-comment">// 业务 逻辑</span>
    <span class="hljs-keyword">return</span> config;
  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-comment">// 业务 逻辑</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;);

<span class="hljs-comment">// 添加响应拦截器</span>
axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
    <span class="hljs-comment">// 业务 逻辑</span>
    <span class="hljs-keyword">return</span> response;
  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-comment">// 业务逻辑</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码，我们可以知道，使用拦截器的时候，只需调用 <code>axios.interceptors</code> 对象上对应方法即可，因此我们可以将这块逻辑抽取出来：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/request/interceptors/index.js</span>
<span class="hljs-keyword">import</span> &#123; log &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../log'</span>;
<span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">'./request/index'</span>;
<span class="hljs-keyword">import</span> response <span class="hljs-keyword">from</span> <span class="hljs-string">'./response/index'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> runInterceptors = <span class="hljs-function"><span class="hljs-params">instance</span> =></span> &#123;
    log(<span class="hljs-string">'[runInterceptors]'</span>, instance);
  <span class="hljs-keyword">if</span>(!instance) <span class="hljs-keyword">return</span>;

    <span class="hljs-comment">// 设置请求拦截器</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> request) &#123;
        instance.interceptors.request
            .use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> request[key](config));
    &#125;

    <span class="hljs-comment">// 设置响应拦截器</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> response) &#123;
        instance.interceptors.response
            .use(<span class="hljs-function"><span class="hljs-params">result</span> =></span> response[key](result));
    &#125;

    <span class="hljs-keyword">return</span> instance;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是我们的<strong>核心拦截器调度器</strong>，目前实现导入所有请求拦截器和响应拦截器后，通过 <code>for</code> 循环，注册所有拦截器，最后将整个 axios 实例返回出去。</p>
<h3 data-id="heading-10">3. 定义简单的请求拦截器和响应拦截器</h3>
<p>这里我们做简单演示，创建以下两个拦截器：</p>
<ol>
<li>请求拦截器：<strong>setLoading</strong>，作用是在发起请求前，显示一个全局 Toast 框，提示“加载中...”文案。</li>
<li>响应拦截器：<strong>setLoading</strong>，作用是在请求响应后，关闭页面中的 Toast 框。</li>
</ol>
<p>为了统一开发规范，我们约定插件开发规范如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/*
  拦截器名称：xxx
*/</span>
<span class="hljs-keyword">const</span> interceptorName = <span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123;
  log(<span class="hljs-string">"[interceptor.request]interceptorName:"</span>, options);
<span class="hljs-comment">// 拦截器业务</span>
  <span class="hljs-keyword">return</span> options;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> interceptorName;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先创建文件 <code>src/request/interceptors/request/</code> 目录下创建 <code>setLoading.js</code>  文件，按照上面约定的插件开发规范，我们完成下面插件开发：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/request/interceptors/request/setLoading.js</span>

<span class="hljs-keyword">import</span> &#123; Toast &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vant'</span>;
<span class="hljs-keyword">import</span> &#123; log &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../../log"</span>;

<span class="hljs-comment">/*
  拦截器名称：全局设置请求的 loading 动画
*/</span>
<span class="hljs-keyword">const</span> setLoading = <span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123;
  log(<span class="hljs-string">"[interceptor.request]setLoading:"</span>, options);

  Toast.loading(&#123;
    <span class="hljs-attr">duration</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'加载中...'</span>,
    <span class="hljs-attr">forbidClick</span>: <span class="hljs-literal">true</span>,
  &#125;);
  <span class="hljs-keyword">return</span> options;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> setLoading;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在导出该请求拦截器，并且导出的是个<strong>数组</strong>，方便拦截器调度器进行统一注册：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/request/interceptors/request/index.js</span>

<span class="hljs-keyword">import</span> setLoading <span class="hljs-keyword">from</span> <span class="hljs-string">'./setLoading'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [
    setLoading
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照相同方式，我们开发响应拦截器：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/request/interceptors/response/setLoading.js</span>

<span class="hljs-keyword">import</span> &#123; Toast &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vant'</span>;
<span class="hljs-keyword">import</span> &#123; log &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../../log"</span>;

<span class="hljs-comment">/*
  拦截器名称：关闭全局请求的 loading 动画
*/</span>
<span class="hljs-keyword">const</span> setLoading = <span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
  log(<span class="hljs-string">"[interceptor.response]setLoading:"</span>, result);

  <span class="hljs-comment">// example: 请求返回成功时，关闭所有 toast 框</span>
  <span class="hljs-keyword">if</span>(result && result.success)&#123;
    Toast.clear();
  &#125;
  <span class="hljs-keyword">return</span> result;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> setLoading;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导出响应拦截器：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/request/interceptors/response/index.js</span>

<span class="hljs-keyword">import</span> setLoading <span class="hljs-keyword">from</span> <span class="hljs-string">'./setLoading'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [
    setLoading
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">4. 全局设置 axios 拦截器</h3>
<p>按照前面相同步骤，我又多写了几个拦截器：
请求拦截器：</p>
<ul>
<li>setSecurityInformation.js：为请求的 url 添加安全参数；</li>
<li>setSignature.js：为请求的请求头添加加签信息；</li>
<li>setToken.js： 为请求的请求头添加 token 信息；</li>
</ul>
<p>响应拦截器：</p>
<ul>
<li>setError.js：处理响应结果的出错情况，如关闭所有 toast 框；</li>
<li>setInvalid.js：处理响应结果的登录失效情况，如跳转到登录页；</li>
<li>setResult.js：处理响应结果的数据嵌套太深的问题，将 <code>result.data.data.data</code> 这类返回结果处理成 <code>result.data</code> 格式；</li>
</ul>
<p>至于是如何实现的，大家有兴趣可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpingan8787%2FLeo-JavaScript%2Fblob%2Fmaster%2FCute-Summary%2Fuseful-request-demo%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pingan8787/Leo-JavaScript/blob/master/Cute-Summary/useful-request-demo/index.html" ref="nofollow noopener noreferrer">在我 Github 查看</a>。</p>
<p>然后我们可以将 axios 进行二次封装，导出 <code>request</code> 对象供业务使用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/request/index.js</span>

<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
<span class="hljs-keyword">import</span> &#123; runInterceptors &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./interceptors/index'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> requestConfig = &#123; <span class="hljs-attr">timeout</span>: <span class="hljs-number">10000</span> &#125;;

<span class="hljs-keyword">let</span> request = axios.create(requestConfig);
request = runInterceptors(request);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> request;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这边就完成。</p>
<p>在业务中需要发起请求，可以这么使用：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div><button @click="send">发起请求</button></div>
</template>

<script setup>
import request from './../request/index.js';

const send = async () => &#123;
  const result = await request(&#123;
    url: 'https://httpbin.org/headers',
    method: 'get'
  &#125;)
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">5. 测试一下</h3>
<p>开发到这边就差不多，我们发送个请求，可以看到所有拦截器执行过程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d35ad954a504d1f9245c9d3fbeee597~tplv-k3u1fbpfcp-zoom-1.image" alt="日志输出" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看看请求头信息：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8308f8e7297f480a88f70716351853b4~tplv-k3u1fbpfcp-zoom-1.image" alt="请求头" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到我们开发的请求拦截器已经生效。</p>
<h2 data-id="heading-13">四、Taro 中使用</h2>
<p>由于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftaro-docs.jd.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://taro-docs.jd.com/" ref="nofollow noopener noreferrer">Taro</a> 中已经提供了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2F2.x%2Fapis%2Fnetwork%2Frequest%2Frequest" target="_blank" rel="nofollow noopener noreferrer" title="https://taro-docs.jd.com/taro/docs/2.x/apis/network/request/request" ref="nofollow noopener noreferrer">Taro.request</a> 方法作为请求方法，我们可以不需要使用 axios 发请求。</p>
<p>基于上面代码进行改造，也很简单，只需要更改 2 个地方：</p>
<h3 data-id="heading-14">1. 修改封装请求的方法</h3>
<p>主要是更换 axios 为 Taro.request 方法，并使用 addInterceptor  方法导入拦截器：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/request/index.js</span>

<span class="hljs-keyword">import</span> Taro <span class="hljs-keyword">from</span> <span class="hljs-string">"@tarojs/taro"</span>;
<span class="hljs-keyword">import</span> &#123; runInterceptors &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./interceptors/index'</span>;

Taro.addInterceptor(runInterceptors);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> request = Taro.request;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> requestTask = Taro.RequestTask; <span class="hljs-comment">// 看需求，是否需要</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> addInterceptor = Taro.addInterceptor; <span class="hljs-comment">// 看需求，是否需要</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">2. 修改拦截器调度器</h3>
<p>由于 axios 和 <code>Taro.request</code> 添加拦截器的方法不同，所以也需要进行更换：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">'./interceptors/request'</span>;
<span class="hljs-keyword">import</span> response <span class="hljs-keyword">from</span> <span class="hljs-string">'./interceptors/response'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> interceptor = &#123;
    request,
    response
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getInterceptor = <span class="hljs-function">(<span class="hljs-params">chain = &#123;&#125;</span>) =></span> &#123;
  <span class="hljs-comment">// 设置请求拦截器</span>
  <span class="hljs-keyword">let</span> requestParams = chain.requestParams;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> request) &#123;
    requestParams = request[key](requestParams);
  &#125;

  <span class="hljs-comment">// 设置响应拦截器</span>
  <span class="hljs-keyword">let</span> responseObject = chain.proceed(requestParams);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> response) &#123;
    responseObject = responseObject.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> response[key](res));
  &#125;
  <span class="hljs-keyword">return</span> responseObject;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体 API 可以看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2F2.x%2Fapis%2Fnetwork%2Frequest%2Frequest" target="_blank" rel="nofollow noopener noreferrer" title="https://taro-docs.jd.com/taro/docs/2.x/apis/network/request/request" ref="nofollow noopener noreferrer">Taro.request</a> 文档，这里不过多介绍。</p>
<h2 data-id="heading-16">五、项目总结和思考</h2>
<p>这次重构主要是按照已有业务进行重构，因此即使是重构后的请求层，仍然还有很多可以优化的点，目前我想到有这些，也算是我的一个 TODO LIST 了：</p>
<h3 data-id="heading-17">1. 将请求层独立成库</h3>
<p>由于公司现在独立站点的项目较多，考虑到项目的统一开发规范，可以考虑将该请求层独立为私有库进行维护。
目前思路：</p>
<ul>
<li>参考插件化架构设计，通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna/" ref="nofollow noopener noreferrer">lerna</a> 做管理所有拦截器；</li>
<li>升级 TypeScript，方便管理和开发；</li>
<li>进行工程化改造，加入构建工具、单元测试、UMD等等；</li>
<li>使用文档和开发文档完善。</li>
</ul>
<h3 data-id="heading-18">2.  支持可更换请求库</h3>
<p>单独抽这一点来讲，是因为目前我们前端团队使用的请求库较多，比较分散，所以考虑到通用性，需要增加支持可更换请求库方法。
目前思路：</p>
<ul>
<li>在已有请求层再抽象一层<strong>请求库适配层</strong>，定义统一接口；</li>
<li>内置几种常见请求库的适配。</li>
</ul>
<h3 data-id="heading-19">3. 开发拦截器脚手架</h3>
<p>这个的目的其实很简单，让团队内其他人直接使用脚手架工具，按照内置脚手架模版，快速创建一个拦截器，进行后续开发，很大程度统一拦截器的开发规范。
目前思路：</p>
<ul>
<li>内置两套拦截器模版：请求拦截器和响应拦截器；</li>
<li>脚手架开发比较简单，参数（如语言）根据业务需要再确定。</li>
</ul>
<h3 data-id="heading-20">4. 增强拦截器调度</h3>
<p>目前实现的这个功能还比较简单，还是得考虑增强拦截器调度。
目前思路：</p>
<ul>
<li>处理拦截器失败的情况；</li>
<li>处理拦截器调度顺序的问题；</li>
<li>拦截器同步执行、异步执行、并发执行、循环执行等等情况；</li>
<li>可插拔的拦截器调度；</li>
<li>考虑参考 Tapable 插件机制；</li>
</ul>
<h2 data-id="heading-21">六、本文总结</h2>
<p>本文通过一次简单的项目重构总结出一个请求层拦截器调度方案，目的是为了实现所有<strong>拦截器职责单一</strong>、方便维护，并<strong>统一维护</strong>和<strong>自动调度</strong>，大大降低实际业务的拦截器开发上手难度。</p>
<p>后续我仍有很多需要优化的地方，作为自己的一个 TODO LIST，如果是做成完全通用，则定位可能更偏向于拦截器调度容器，只提供一些通用拦截器，其余还是由开发者定义，库负责调度，但常用的请求库一般都已经做好，所以这样做的价值有待权衡。</p>
<p>当然，目前还是优先作为团队内部私有库进行开发和使用，因为基本上团队内部使用的业务都差不多，只是项目不同。</p></div>  
</div>
            