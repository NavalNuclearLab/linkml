
# Class: anonymous_expression

An abstract parent class for any nested expression

URI: [linkml:AnonymousExpression](https://w3id.org/linkml/AnonymousExpression)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetDefinition],[StructuredAlias],[Extension],[Extensible],[Expression],[Example],[CommonMetadata],[AnonymousSlotExpression],[AnonymousExpression&#124;description:string%20%3F;title:string%20%3F;deprecated:string%20%3F;todos:string%20*;notes:string%20*;comments:string%20*;from_schema:uri%20%3F;imported_from:string%20%3F;source:uriorcurie%20%3F;in_language:string%20%3F;see_also:uriorcurie%20*;deprecated_element_has_exact_replacement:uriorcurie%20%3F;deprecated_element_has_possible_replacement:uriorcurie%20%3F;aliases:string%20*;mappings:uriorcurie%20*;exact_mappings:uriorcurie%20*;close_mappings:uriorcurie%20*;related_mappings:uriorcurie%20*;narrow_mappings:uriorcurie%20*;broad_mappings:uriorcurie%20*;created_by:uriorcurie%20%3F;contributors:uriorcurie%20*;created_on:datetime%20%3F;last_updated_on:datetime%20%3F;modified_by:uriorcurie%20%3F;status:uriorcurie%20%3F;rank:integer%20%3F;categories:uriorcurie%20*;keywords:string%20*]uses%20-.->[Expression],[AnonymousExpression]uses%20-.->[Extensible],[AnonymousExpression]uses%20-.->[Annotatable],[AnonymousExpression]uses%20-.->[CommonMetadata],[AnonymousExpression]^-[AnonymousSlotExpression],[AnonymousExpression]^-[AnonymousClassExpression],[AnonymousClassExpression],[Annotation],[Annotatable],[AltDescription])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetDefinition],[StructuredAlias],[Extension],[Extensible],[Expression],[Example],[CommonMetadata],[AnonymousSlotExpression],[AnonymousExpression&#124;description:string%20%3F;title:string%20%3F;deprecated:string%20%3F;todos:string%20*;notes:string%20*;comments:string%20*;from_schema:uri%20%3F;imported_from:string%20%3F;source:uriorcurie%20%3F;in_language:string%20%3F;see_also:uriorcurie%20*;deprecated_element_has_exact_replacement:uriorcurie%20%3F;deprecated_element_has_possible_replacement:uriorcurie%20%3F;aliases:string%20*;mappings:uriorcurie%20*;exact_mappings:uriorcurie%20*;close_mappings:uriorcurie%20*;related_mappings:uriorcurie%20*;narrow_mappings:uriorcurie%20*;broad_mappings:uriorcurie%20*;created_by:uriorcurie%20%3F;contributors:uriorcurie%20*;created_on:datetime%20%3F;last_updated_on:datetime%20%3F;modified_by:uriorcurie%20%3F;status:uriorcurie%20%3F;rank:integer%20%3F;categories:uriorcurie%20*;keywords:string%20*]uses%20-.->[Expression],[AnonymousExpression]uses%20-.->[Extensible],[AnonymousExpression]uses%20-.->[Annotatable],[AnonymousExpression]uses%20-.->[CommonMetadata],[AnonymousExpression]^-[AnonymousSlotExpression],[AnonymousExpression]^-[AnonymousClassExpression],[AnonymousClassExpression],[Annotation],[Annotatable],[AltDescription])

## Uses Mixin

 *  mixin: [Expression](Expression.md) - general mixin for any class that can represent some form of expression
 *  mixin: [Extensible](Extensible.md) - mixin for classes that support extension
 *  mixin: [Annotatable](Annotatable.md) - mixin for classes that support annotations
 *  mixin: [CommonMetadata](CommonMetadata.md) - Generic metadata shared across definitions

## Children

 * [AnonymousClassExpression](AnonymousClassExpression.md)
 * [AnonymousSlotExpression](AnonymousSlotExpression.md)

## Referenced by Class


## Attributes


### Mixed in from extensible:

 * [extensions](extensions.md)  <sub>0..\*</sub>
     * Description: a tag/text tuple attached to an arbitrary element
     * Range: [Extension](Extension.md)

### Mixed in from annotatable:

 * [annotations](annotations.md)  <sub>0..\*</sub>
     * Description: a collection of tag/text tuples with the semantics of OWL Annotation
     * Range: [Annotation](Annotation.md)

### Mixed in from common_metadata:

 * [description](description.md)  <sub>0..1</sub>
     * Description: a textual description of the element's purpose and use
     * Range: [String](types/String.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [alt_descriptions](alt_descriptions.md)  <sub>0..\*</sub>
     * Description: A sourced alternative description for an element
     * Range: [AltDescription](AltDescription.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [title](title.md)  <sub>0..1</sub>
     * Description: A concise human-readable display label for the element. The title should mirror the name, and should use ordinary textual punctuation.
     * Range: [String](types/String.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [deprecated](deprecated.md)  <sub>0..1</sub>
     * Description: Description of why and when this element will no longer be used
     * Range: [String](types/String.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [todos](todos.md)  <sub>0..\*</sub>
     * Description: Outstanding issues that needs resolution
     * Range: [String](types/String.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [notes](notes.md)  <sub>0..\*</sub>
     * Description: editorial notes about an element intended primarily for internal consumption
     * Range: [String](types/String.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [comments](comments.md)  <sub>0..\*</sub>
     * Description: notes and comments about an element intended primarily for external consumption
     * Range: [String](types/String.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [examples](examples.md)  <sub>0..\*</sub>
     * Description: example usages of an element
     * Range: [Example](Example.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [in_subset](in_subset.md)  <sub>0..\*</sub>
     * Description: used to indicate membership of a term in a defined subset of terms used for a particular domain or application.
     * Range: [SubsetDefinition](SubsetDefinition.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [from_schema](from_schema.md)  <sub>0..1</sub>
     * Description: id of the schema that defined the element
     * Range: [Uri](types/Uri.md)
     * in subsets: (SpecificationSubset)

### Mixed in from common_metadata:

 * [imported_from](imported_from.md)  <sub>0..1</sub>
     * Description: the imports entry that this element was derived from.  Empty means primary source
     * Range: [String](types/String.md)

### Mixed in from common_metadata:

 * [source](source.md)  <sub>0..1</sub>
     * Description: A related resource from which the element is derived.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [in_language](in_language.md)  <sub>0..1</sub>
     * Description: the primary language used in the sources
     * Range: [String](types/String.md)

### Mixed in from common_metadata:

 * [see_also](see_also.md)  <sub>0..\*</sub>
     * Description: A list of related entities or URLs that may be of relevance
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [deprecated element has exact replacement](deprecated_element_has_exact_replacement.md)  <sub>0..1</sub>
     * Description: When an element is deprecated, it can be automatically replaced by this uri or curie
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from common_metadata:

 * [deprecated element has possible replacement](deprecated_element_has_possible_replacement.md)  <sub>0..1</sub>
     * Description: When an element is deprecated, it can be potentially replaced by this uri or curie
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from common_metadata:

 * [aliases](aliases.md)  <sub>0..\*</sub>
     * Description: Alternate names/labels for the element. These do not alter the semantics of the schema, but may be useful to support search and alignment.
     * Range: [String](types/String.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [structured_aliases](structured_aliases.md)  <sub>0..\*</sub>
     * Description: A list of structured_alias objects, used to provide aliases in conjunction with additional metadata.
     * Range: [StructuredAlias](StructuredAlias.md)

### Mixed in from common_metadata:

 * [mappings](mappings.md)  <sub>0..\*</sub>
     * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from common_metadata:

 * [exact mappings](exact_mappings.md)  <sub>0..\*</sub>
     * Description: A list of terms from different schemas or terminology systems that have identical meaning.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from common_metadata:

 * [close mappings](close_mappings.md)  <sub>0..\*</sub>
     * Description: A list of terms from different schemas or terminology systems that have close meaning.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from common_metadata:

 * [related mappings](related_mappings.md)  <sub>0..\*</sub>
     * Description: A list of terms from different schemas or terminology systems that have related meaning.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from common_metadata:

 * [narrow mappings](narrow_mappings.md)  <sub>0..\*</sub>
     * Description: A list of terms from different schemas or terminology systems that have narrower meaning.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from common_metadata:

 * [broad mappings](broad_mappings.md)  <sub>0..\*</sub>
     * Description: A list of terms from different schemas or terminology systems that have broader meaning.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Mixed in from common_metadata:

 * [created_by](created_by.md)  <sub>0..1</sub>
     * Description: agent that created the element
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [contributors](contributors.md)  <sub>0..\*</sub>
     * Description: agent that contributed to the element
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [created_on](created_on.md)  <sub>0..1</sub>
     * Description: time at which the element was created
     * Range: [Datetime](types/Datetime.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [last_updated_on](last_updated_on.md)  <sub>0..1</sub>
     * Description: time at which the element was last updated
     * Range: [Datetime](types/Datetime.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [modified_by](modified_by.md)  <sub>0..1</sub>
     * Description: agent that modified the element
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [status](status.md)  <sub>0..1</sub>
     * Description: status of the element
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * Example: bibo:draft None
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [rank](rank.md)  <sub>0..1</sub>
     * Description: the relative order in which the element occurs, lower values are given precedence
     * Range: [Integer](types/Integer.md)
     * in subsets: (SpecificationSubset,BasicSubset)

### Mixed in from common_metadata:

 * [categories](categories.md)  <sub>0..\*</sub>
     * Description: Controlled terms used to categorize an element.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (BasicSubset)

### Mixed in from common_metadata:

 * [keywords](keywords.md)  <sub>0..\*</sub>
     * Description: Keywords or tags used to describe the element
     * Range: [String](types/String.md)
     * in subsets: (BasicSubset)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | anonymous expressions are useful for when it is necessary to build a complex expression without introducing a named element for each sub-expression |
