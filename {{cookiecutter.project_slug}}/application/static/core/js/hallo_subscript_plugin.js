(function () {
    (function ($) {
        return $.widget('IKS.subscript', {
            options: {
                uuid: '',
                tag: 'sub',
                editable: null,
                buttonCssClass: null
            },

            inContext: function () {
                var widget = this;
                var node = widget.options.editable.getSelection().commonAncestorContainer;
                return $(node).parents(widget.options.tag).get(0);
            },

            populateToolbar: function (toolbar) {

                var widget = this;
                var button = $('<span></span>');

                button.hallobutton({
                    uuid: this.options.uuid,
                    editable: this.options.editable,
                    cssClass: this.options.buttonCssClass,
                    command: null,
                    label: 'Subscript',
                    icon: 'icon-order-down',
                    queryState: function (event) {
                        return button.hallobutton('checked', !!widget.inContext());
                    }
                });

                toolbar.append(button);

                button.on('click', function (event) {
                    return widget.options.editable.execute(
                        widget.inContext() ? 'removeFormat' : 'subscript'
                    );
                });

            }
        });
    })(jQuery);
}).call(this);